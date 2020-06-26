import numpy as np
from napari_tifffile import napari_get_reader
import tifffile


def test_reader(tmp_path):
    """An example of how you might test your plugin."""

    my_test_file = str(tmp_path / "myfile.tif")
    original_data = np.random.rand(20, 20)
    tifffile.imwrite(my_test_file, original_data)

    # try to read it back in
    reader = napari_get_reader(my_test_file)
    assert callable(reader)

    # make sure we're delivering the right format
    layer_data_list = reader(my_test_file)
    assert isinstance(layer_data_list, list) and len(layer_data_list) > 0
    layer_data_tuple = layer_data_list[0]
    assert isinstance(layer_data_tuple, tuple) and len(layer_data_tuple) > 0

    # make sure it's the same as it started
    np.testing.assert_allclose(original_data, layer_data_tuple[0])


def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None
