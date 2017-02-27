# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..misc import Overlap


def test_Overlap_inputs():
    input_map = dict(bg_overlap=dict(mandatory=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    mask_volume=dict(),
    out_file=dict(usedefault=True,
    ),
    vol_units=dict(mandatory=True,
    usedefault=True,
    ),
    volume1=dict(mandatory=True,
    ),
    volume2=dict(mandatory=True,
    ),
    weighting=dict(usedefault=True,
    ),
    )
    inputs = Overlap.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Overlap_outputs():
    output_map = dict(dice=dict(),
    diff_file=dict(),
    jaccard=dict(),
    labels=dict(),
    roi_di=dict(),
    roi_ji=dict(),
    roi_voldiff=dict(),
    volume_difference=dict(),
    )
    outputs = Overlap.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value