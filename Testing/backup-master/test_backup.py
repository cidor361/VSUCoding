import unittest
from backup import *



class test_backup(unittest.TestCase):

    tarpattern = re.compile('{0}-\d{{4}}-\d{{2}}-\d{{2}}-\d{{3,}}'.format(socket.gethostname()))

    def test_get_archive_name(self):
        self.assertEqual(get_archive_name('test', False), 'test/Zbook-2021-03-13-000.tar')

    def test_archive_files(self):
        name = get_archive_name('test', False)
        self.assertEqual(archive_files('test/test.txt', name), True)

    def test_list_archives(self):
        self.assertEqual(list_archives('test', self.tarpattern), ['test/Zbook-2021-03-13-000.tar'])

    def test_extract_files(self):
        self.assertEqual(extract_files('test/Zbook-2021-03-13-000.tar', '/test/extracted'), True)

    def test_purge_archives(self):
        self.assertEqual(purge_archives('test', 1), True)

