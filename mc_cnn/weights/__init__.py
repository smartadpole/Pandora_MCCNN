#!/usr/bin/env python
# coding: utf8
#
# Copyright (c) 2015, Jure Zbontar <jure.zbontar@gmail.com>
# Copyright (c) 2021 Centre National d'Etudes Spatiales (CNES).
#
# This file is part of PANDORA_MCCNN
#
#     https://github.com/CNES/Pandora_MCCNN
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
This module contains all functions to access MC-CNN weights
"""

import importlib_resources

AVAILABLE_WEIGHTS = {
    "fast": {
        "middlebury": "mc_cnn_fast_mb_weights.pt",
        "dfc": "mc_cnn_fast_data_fusion_contest.pt"
    },
    "accurate": {
        "middlebury": "mc_cnn_accurate_mb_weights.pt",
        "dfc": "mc_cnn_accurate_data_fusion_contest.pt"
    }
}

def get_weights(arch="fast", training_dataset="middlebury"):
    filename = AVAILABLE_WEIGHTS[arch][training_dataset]
    return importlib_resources.files("mc_cnn.weights").joinpath(filename)