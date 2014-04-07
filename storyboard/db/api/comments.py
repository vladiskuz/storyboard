# Copyright (c) 2014 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from storyboard.db.api import base as api_base
from storyboard.db import models


def comment_get(comment_id):
    return api_base.entity_get(models.Comment, comment_id)


def comment_get_all(marker=None, limit=None, **kwargs):
    return api_base.entity_get_all(models.Comment,
                                   is_active=True,
                                   marker=marker,
                                   limit=limit,
                                   **kwargs)


def comment_get_count(**kwargs):
    return api_base.entity_get_count(models.Comment,
                                     is_active=True,
                                     **kwargs)


def comment_create(values):
    return api_base.entity_create(models.Comment, values)


def comment_update(comment_id, values):
    return api_base.entity_update(models.Comment, comment_id, values)


def comment_delete(comment_id):
    comment = comment_get(comment_id)

    if comment:
        comment.is_active = False
        api_base.entity_update(models.Task, comment_id, comment.as_dict())