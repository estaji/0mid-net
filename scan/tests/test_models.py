from datetime import datetime

from django.test import TestCase

from scan.models import Job, Node, ScanConfig


class NodeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Node.objects.create(
            node_type="p",
            location="IR-Parseh",
            url="www.srv.mysite.com",
            is_active=True,
        )
        Node.objects.create(
            node_type="c",
            location="USA-LA",
            url="www.srv2.mysite.com",
            is_active=True,
        )

    def test_add_parent_node(self):
        """Test add parent node"""
        item = Node.objects.filter(node_type="p").first()

        self.assertEqual(item.node_type, "p")
        self.assertEqual(item.location, "IR-Parseh")
        self.assertEqual(item.url, "www.srv.mysite.com")
        self.assertEqual(item.is_active, True)

    def test_add_child_node(self):
        """Test add child node"""
        item = Node.objects.filter(node_type="c").first()

        self.assertEqual(item.node_type, "c")
        self.assertEqual(item.location, "USA-LA")
        self.assertEqual(item.url, "www.srv2.mysite.com")
        self.assertEqual(item.is_active, True)


class JobModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Node.objects.create(
            node_type="p",
            location="IR-Parseh",
            url="www.srv.mysite.com",
            is_active=True,
        )
        Job.objects.create(
            start_time=datetime.now(),
            command="pi",
            node=Node.objects.get(id=1),
            uuid="07379a5f-7dfe-4efa-a8c5-038dbffd7da0",
            url="www.e-damavandihe.ac.ir",
        )
        Job.objects.create(
            start_time=datetime.now(),
            command="pi",
            node=Node.objects.get(id=1),
            status="s",
            uuid="07388a5f-1dfe-aefa-b8c5-660dbffd7da0",
            url="www.bing.com",
        )
        Job.objects.create(
            start_time=datetime.now(),
            command="p",
            node=Node.objects.get(id=1),
            status="s",
            uuid="07388a5f-1dfe-aefa-b8c5-660dbffd7da0",
            url="www.bing.com",
            result="Ping OK",
        )
        Job.objects.create(
            start_time=datetime.now(),
            command="hi",
            node=Node.objects.get(id=1),
            status="n",
            uuid="9bd39a02-3ab5-4fce-8155-f3f1c97c9543",
            url="stackoverflow.com",
        )
        Job.objects.create(
            start_time=datetime.now(),
            command="si",
            node=Node.objects.get(id=1),
            status="n",
            uuid="9bd22a02-3ab2-4fce-8155-f3f1c97c9543",
            url="sslshopper.com",
        )
        Job.objects.create(
            start_time=datetime.now(),
            command="s",
            node=Node.objects.get(id=1),
            status="n",
            uuid="9bd22a02-3ab2-4fce-8155-f3f1c97c9543",
            url="sslshopper.com",
        )

    def test_add_job(self):
        """Test add a scan job"""
        item = Job.objects.get(id=1)

        self.assertEqual(item.command, "pi")
        self.assertEqual(item.node, Node.objects.get(id=1))
        self.assertEqual(str(item.uuid), "07379a5f-7dfe-4efa-a8c5-038dbffd7da0")
        self.assertEqual(item.url, "www.e-damavandihe.ac.ir")

    def test_add_http_job(self):
        """Test add a http scan job"""
        item = Job.objects.get(id=4)

        self.assertEqual(item.command, "hi")
        self.assertEqual(item.status, "n")
        self.assertEqual(str(item.uuid), "9bd39a02-3ab5-4fce-8155-f3f1c97c9543")
        self.assertEqual(item.url, "stackoverflow.com")

    def test_add_ssl_job(self):
        """Test add a ssl (si) scan job"""
        item = Job.objects.get(id=5)

        self.assertEqual(item.command, "si")
        self.assertEqual(item.status, "n")
        self.assertEqual(str(item.uuid), "9bd22a02-3ab2-4fce-8155-f3f1c97c9543")
        self.assertEqual(item.url, "sslshopper.com")

    def test_add_ssl_child_job(self):
        """Test add a ssl (s) scan job"""
        item = Job.objects.get(id=6)

        self.assertEqual(item.command, "s")
        self.assertEqual(item.status, "n")
        self.assertEqual(str(item.uuid), "9bd22a02-3ab2-4fce-8155-f3f1c97c9543")
        self.assertEqual(item.url, "sslshopper.com")

    def test_uuid_result_jobs_func(self):
        """Test get a uuid and return jobs of the uuid"""
        items = Job.uuid_result_jobs("07388a5f-1dfe-aefa-b8c5-660dbffd7da0")

        self.assertNotEqual(items[0].result, "")
        self.assertEqual(items[0].status, "s")
        self.assertEqual(str(items[0].uuid), "07388a5f-1dfe-aefa-b8c5-660dbffd7da0")

    def test_uuid_children_count_func(self):
        """Test get a uuid and return number of child/children jobs"""
        the_uuid = "07388a5f-1dfe-aefa-b8c5-660dbffd7da0"
        item = Job.uuid_children_count(the_uuid)
        alljobs = Job.objects.filter(uuid=the_uuid).count()
        children = alljobs - 1

        self.assertEqual(item, children)

    def test_url_of_uuid(self):
        """Test get a uuid and return url of it"""
        the_uuid = "07388a5f-1dfe-aefa-b8c5-660dbffd7da0"
        item = Job.url_of_uuid(the_uuid)
        item2 = Job.objects.filter(uuid=the_uuid).latest("add_time")

        self.assertEqual(item, item2.url)


class ScanConfigModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        ScanConfig.objects.create(
            title="Website Title",
            description="This a service for scanning",
            keywords="scan, scanner, online service",
        )

    def test_add_scan_config(self):
        """Test add parent node"""
        item = ScanConfig.objects.get(id=1)

        self.assertEqual(item.title, "Website Title")
        self.assertEqual(item.description, "This a service for scanning")
        self.assertEqual(item.keywords, "scan, scanner, online service")
