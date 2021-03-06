
from unittest import TestCase
import unittest
import pygem.file_handler as fh
import numpy as np


class TestFileHandler(TestCase):


	def test_base_class_members(self):
		file_handler = fh.FileHandler()
		assert file_handler.file == None
		assert file_handler.filename == None
		assert file_handler.extension == None

	
	def test_base_class_parse(self):
		file_handler = fh.FileHandler()
		with self.assertRaises(NotImplementedError):
			file_handler.parse()


	def test_base_class_write(self):
		file_handler = fh.FileHandler()
		with self.assertRaises(NotImplementedError):
			file_handler.write()
	

	def test_unv_file_member(self):
		unv_handler = fh.UnvHandler('tests/test_datasets/test_square.unv')
		assert unv_handler.file == None


	def test_unv_filename_member(self):
		unv_handler = fh.UnvHandler('tests/test_datasets/test_square.unv')
		assert unv_handler.filename == 'tests/test_datasets/test_square.unv'
	

	def test_unv_extension_member(self):
		unv_handler = fh.UnvHandler('tests/test_datasets/test_square.unv')
		assert unv_handler.extension == 'unv'


	def test_unv_failing_filename_type(self):
		with self.assertRaises(TypeError):
			unv_handler = fh.UnvHandler(3)


	def test_unv_instantiation(self):
		unv_handler = fh.UnvHandler('tests/test_datasets/test_square.unv')
	

	def test_unv_failing_check_extension(self):
		with self.assertRaises(ValueError):
			unv_handler = fh.UnvHandler('tests/test_datasets/test_square.iges')


	def test_unv_parse_shape(self):
		unv_handler = fh.UnvHandler('tests/test_datasets/test_square.unv')
		mesh_points = unv_handler.parse()
		assert mesh_points.shape == (256, 3)


	def test_unv_parse_coords_1(self):
		unv_handler = fh.UnvHandler('tests/test_datasets/test_square.unv')
		mesh_points = unv_handler.parse()
		np.testing.assert_almost_equal(abs(mesh_points[33][0]), 1.0)


	def test_unv_parse_coords_2(self):
		unv_handler = fh.UnvHandler('tests/test_datasets/test_square.unv')
		mesh_points = unv_handler.parse()
		np.testing.assert_almost_equal(abs(mesh_points[178][1]), 0.4)


	def test_unv_parse_coords_3(self):
		unv_handler = fh.UnvHandler('tests/test_datasets/test_square.unv')
		mesh_points = unv_handler.parse()
		np.testing.assert_almost_equal(abs(mesh_points[100][2]), 0.0)		



