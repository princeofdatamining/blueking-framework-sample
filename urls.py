# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

urls config
"""
from django.urls import include, path
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

prefix = settings.SITE_URL.lstrip('/')

# 公共URL配置
urlpatterns = [
    path(prefix + 'admin/', admin.site.urls),
    path(prefix + 'auth/', include('rest_framework.urls')),
    path(prefix, include('home_application.urls')),
]
