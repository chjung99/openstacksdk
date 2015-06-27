# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.image import image_service
from openstack import resource


class Member(resource.Resource):
    id_attribute = 'member_id'
    resources_key = 'members'
    base_path = '/images/%(image_id)/members'
    service = image_service.ImageService()

    # capabilities
    allow_create = True
    allow_retrieve = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # Properties
    #: The date and time when the member was created.
    created_at = resource.prop('created_at')
    #: Image ID stored through the image API. Typically a UUID.
    image_id = resource.prop('image_id')
    #: The status of the image.
    status = resource.prop('status')
    #: The date and time when the member was updated.
    updated_at = resource.prop('updated_at')
