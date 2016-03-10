# standard libraries
import functools

# third party libraries
import numpy

# local libraries
from nion.data import Core
from nion.data import DataAndMetadata

def context():
    g = dict()

    # data type constants
    g["int16"] = numpy.int16
    g["int32"] = numpy.int32
    g["int64"] = numpy.int64
    g["uint8"] = numpy.uint8
    g["uint16"] = numpy.uint16
    g["uint32"] = numpy.uint32
    g["uint64"] = numpy.uint64
    g["float32"] = numpy.float32
    g["float64"] = numpy.float64
    g["complex64"] = numpy.complex64
    g["complex128"] = numpy.complex128

    # functions changing size or type of array
    g["data_shape"] = Core.data_shape
    g["astype"] = functools.partial(Core.function_array, Core.astype)
    g["concatenate"] = Core.function_concatenate
    g["reshape"] = Core.function_reshape
    g["data_slice"] = DataAndMetadata.function_data_slice
    g["item"] = Core.take_item
    g["crop"] = Core.function_crop
    g["slice_sum"] = Core.function_slice_sum
    g["pick"] = Core.function_pick
    g["project"] = Core.function_project
    g["resample_image"] = Core.function_resample_2d
    g["newaxis"] = numpy.newaxis

    # functions generating arrays
    g["column"] = Core.column
    g["row"] = Core.row
    g["radius"] = Core.radius

    # functions taking array and producing scalars
    g["amin"] = functools.partial(Core.function_scalar, numpy.amin)
    g["amax"] = functools.partial(Core.function_scalar, numpy.amax)
    g["arange"] = functools.partial(Core.function_scalar, numpy.arange)
    g["median"] = functools.partial(Core.function_scalar, numpy.median)
    g["average"] = functools.partial(Core.function_scalar, numpy.average)
    g["mean"] = functools.partial(Core.function_scalar, numpy.mean)
    g["std"] = functools.partial(Core.function_scalar, numpy.std)
    g["var"] = functools.partial(Core.function_scalar, numpy.var)

    # trig array functions
    g["sin"] = functools.partial(Core.function_array, numpy.sin)
    g["cos"] = functools.partial(Core.function_array, numpy.cos)
    g["tan"] = functools.partial(Core.function_array, numpy.tan)
    g["arcsin"] = functools.partial(Core.function_array, numpy.arcsin)
    g["arccos"] = functools.partial(Core.function_array, numpy.arccos)
    g["arctan"] = functools.partial(Core.function_array, numpy.arctan)
    g["hypot"] = functools.partial(Core.function_array, numpy.hypot)
    g["arctan2"] = functools.partial(Core.function_array, numpy.arctan2)
    g["degrees"] = functools.partial(Core.function_array, numpy.degrees)
    g["radians"] = functools.partial(Core.function_array, numpy.radians)
    g["rad2deg"] = functools.partial(Core.function_array, numpy.rad2deg)
    g["deg2rad"] = functools.partial(Core.function_array, numpy.deg2rad)

    # rounding
    g["around"] = functools.partial(Core.function_array, numpy.around)
    g["round"] = functools.partial(Core.function_array, numpy.round)
    g["rint"] = functools.partial(Core.function_array, numpy.rint)
    g["fix"] = functools.partial(Core.function_array, numpy.fix)
    g["floor"] = functools.partial(Core.function_array, numpy.floor)
    g["ceil"] = functools.partial(Core.function_array, numpy.ceil)
    g["trunc"] = functools.partial(Core.function_array, numpy.trunc)

    # exponents and logarithms
    g["exp"] = functools.partial(Core.function_array, numpy.exp)
    g["expm1"] = functools.partial(Core.function_array, numpy.expm1)
    g["exp2"] = functools.partial(Core.function_array, numpy.exp2)
    g["log"] = functools.partial(Core.function_array, numpy.log)
    g["log10"] = functools.partial(Core.function_array, numpy.log10)
    g["log2"] = functools.partial(Core.function_array, numpy.log2)
    g["log1p"] = functools.partial(Core.function_array, numpy.log1p)

    # other functions
    g["reciprocal"] = functools.partial(Core.function_array, numpy.reciprocal)
    g["clip"] = functools.partial(Core.function_array, numpy.clip)
    g["sqrt"] = functools.partial(Core.function_array, numpy.sqrt)
    g["square"] = functools.partial(Core.function_array, numpy.square)
    g["nan_to_num"] = functools.partial(Core.function_array, numpy.nan_to_num)

    # complex numbers
    g["angle"] = functools.partial(Core.function_array, numpy.angle)
    g["real"] = functools.partial(Core.function_array, numpy.real)
    g["imag"] = functools.partial(Core.function_array, numpy.imag)
    g["conj"] = functools.partial(Core.function_array, numpy.conj)

    # ffts
    g["fft"] = Core.function_fft
    g["ifft"] = Core.function_ifft
    g["autocorrelate"] = Core.function_autocorrelate
    g["crosscorrelate"] = Core.function_crosscorrelate

    # filters
    g["sobel"] = Core.function_sobel
    g["laplace"] = Core.function_laplace
    g["gaussian_blur"] = Core.function_gaussian_blur
    g["median_filter"] = Core.function_median_filter
    g["uniform_filter"] = Core.function_uniform_filter
    g["transpose_flip"] = Core.function_transpose_flip

    # miscellaneous
    g["histogram"] = Core.function_histogram
    g["line_profile"] = Core.function_line_profile

    # g["data_by_uuid"] = lambda data_uuid: data_by_uuid(context, data_uuid)
    # g["region_by_uuid"] = lambda region_uuid: region_by_uuid(context, region_uuid)

    # geometry functions
    g["shape"] = Core.function_make_shape
    g["rectangle_from_origin_size"] = Core.function_make_rectangle_origin_size
    g["rectangle_from_center_size"] = Core.function_make_rectangle_center_size
    g["vector"] = Core.function_make_vector
    g["normalized_point"] = Core.function_make_point
    g["normalized_size"] = Core.function_make_size
    g["normalized_interval"] = Core.function_make_interval

    class ContextObject:
        def __init__(self):
            self.g = g
    ctx = ContextObject()
    for k, v in g.items():
        setattr(ctx, k, v)
    return ctx