import chainer


def concat_mols(batch, device=None, padding=0):
    """Concatenates a list of molecules into array(s).

    This function converts "an arrays of tuples" into "a tuple of arrays".
    Given an list of examples each of which consists of
    multiple arrays, this function takes an array in the same "relative"
    position within an example from each example, concatenates them along the
    newly-inserted first axis (called `batch dimension`) into one array.
    It does the same thing with all positions, and returns resulting arrays.

    The output type depends on the type of examples in ``batch``.
    For instance, consider each example consists of two arrays ``(x, y)``.
    Then, this function concatenates ``x`` 's into one array, and ``y`` 's
    into another array, and returns a tuple of these two arrays. Another
    example: consider each example is a dictionary of two entries whose keys
    are ``'x'`` and ``'y'``, respectively, and values are arrays. Then, this
    function concatenates ``x`` 's into one array, and ``y`` 's into another
    array, and returns a dictionary with two entries ``x`` and ``y`` whose
    values are the concatenated arrays.

    When the arrays to concatenate have different shapes, the behavior depends
    on the ``padding`` value. If ``padding`` is ``None`` (default), it raises
    an error. Otherwise, it builds an array of the minimum shape that the
    contents of all arrays can be substituted to. The padding value is then
    used to the extra elements of the resulting arrays.

    The current implementation is identical to
    :func:`~chainer.dataset.concat_examples` of Chainer, except the default
    value of the ``padding`` option is changed to ``0``.

    .. seealso:: :func:`chainer.dataset.concat_examples`

    Args:
        batch (list):
            A list of examples. This is typically given by a dataset
            iterator.
        device (int):
            Device ID to which each array is sent. Negative value
            indicates the host memory (CPU). If it is omitted, all arrays are
            left in the original device.
        padding:
            Scalar value for extra elements. If this is None (default),
            an error is raised on shape mismatch. Otherwise, an array of
            minimum dimensionalities that can accommodate all arrays is
            created, and elements outside of the examples are padded by this
            value.

    Returns:
        Array, a tuple of arrays, or a dictionary of arrays:
        The type depends on the type of each example in the batch.
    """
    return chainer.dataset.concat_examples(batch, device, padding=padding)
