import logging
from datetime import datetime
from uuid import uuid4

from django.db import transaction
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import CoreConfig, Menu, SubMenu

from .form import ScanForm
from .models import Job, Node, ScanConfig
from .utils import http_check, pinging

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    """View for scan page"""

    template_name = "scan/home.html"
    form_class = ScanForm

    def post(self, request, *args, **kwargs):
        """User posts it's url for scanning (add a new job for it)"""
        form = self.form_class(request.POST)
        if form.is_valid():
            with transaction.atomic():
                url = form.cleaned_data["url"]
                action = form.cleaned_data["action"]
                logger.debug("form action is {}".format(action))
                newjob = Job()
                newjob.start_time = datetime.now()
                newjob.command = action
                newjob.node = Node.objects.get(node_type="p")
                newjob.uuid = uuid4()
                newjob.url = url
                newjob.save()
                logger.info("form is valid and newjob saved {{{}}}".format(url))
            return redirect("scan:result", uuid=newjob.uuid)

        logger.warn("form is NOT valid {{{}}}".format(request.POST.get("url")))
        context = super().get_context_data(**kwargs)
        context["core_conf"] = CoreConfig.objects.all()
        context["menu_parent"] = Menu.objects.filter(icon_type="DD")
        context["menu_single"] = Menu.objects.filter(icon_type="N")
        context["menu_disabled"] = Menu.objects.filter(icon_type="DI")
        context["submenu"] = SubMenu.objects.all()
        context["configs"] = ScanConfig.objects.all()
        context["form"] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["core_conf"] = CoreConfig.objects.all()
        context["menu_parent"] = Menu.objects.filter(icon_type="DD")
        context["menu_single"] = Menu.objects.filter(icon_type="N")
        context["menu_disabled"] = Menu.objects.filter(icon_type="DI")
        context["submenu"] = SubMenu.objects.all()
        context["configs"] = ScanConfig.objects.all()
        context["active_nodes"] = Node.objects.filter(is_active=True)

        return context


class ResultView(TemplateView):
    """View for result page which user redirected to it
    based on uuid after posting a url"""

    template_name = "scan/result.html"

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context["core_conf"] = CoreConfig.objects.all()
            context["menu_parent"] = Menu.objects.filter(icon_type="DD")
            context["menu_single"] = Menu.objects.filter(icon_type="N")
            context["menu_disabled"] = Menu.objects.filter(icon_type="DI")
            context["submenu"] = SubMenu.objects.all()
            context["configs"] = ScanConfig.objects.all()

            uuid = self.kwargs["uuid"]
            context["uuid"] = uuid
            context["results"] = Job.uuid_result_jobs(uuid)
            context["site_url"] = Job.url_of_uuid(uuid)
            child_count = Job.uuid_children_count(uuid)
            try:
                calc = Job.uuid_result_jobs(uuid).count() * 100
                progress = calc / child_count
            except ZeroDivisionError:
                progress = 0
            context["progress"] = progress
            return context
        except Job.DoesNotExist:
            raise Http404


class FreshResultView(TemplateView):
    """View for returning new results to template based on htmx"""

    template_name = "scan/fresh_result.html"

    def get(self, request, *args, **kwargs):
        try:
            context = self.get_context_data(**kwargs)
            uuid = self.kwargs["uuid"]
            context["results"] = Job.uuid_result_jobs(uuid)
            child_count = Job.uuid_children_count(uuid)
            try:
                calc = Job.uuid_result_jobs(uuid).count() * 100
                progress = calc / child_count
            except ZeroDivisionError:
                progress = 0
            context["progress"] = progress
            if progress == 100:
                logger.info("a 100% job finished and 286 returned to client")
                return self.render_to_response(context, status=286)
            else:
                return self.render_to_response(context, status=200)
        except Job.DoesNotExist:
            raise Http404


class PingView(APIView):
    """Get request from parent, do PING and return result"""

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        query_string = request.GET.get("url", None)

        if query_string:
            result = pinging(query_string)
            logger.info("pinging api view finished {{{}}}".format(query_string))
            content = {"result": "{}".format(result)}
            return Response(content)

        else:
            logger.error("pinging api needs a url")
            content = {"result": "Need a url"}
            return Response(content)


class HttpView(APIView):
    """Get request from parent, do Http check and return result"""

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        query_string = request.GET.get("url", None)

        if query_string:
            result = http_check(query_string)
            content = {"result": "{}".format(result)}
            logger.info("http_checked api view finished {{{}}}".format(query_string))
            return Response(content)

        else:
            logger.error("http_check api needs a url")
            content = {"result": "Need a url"}
            return Response(content)
