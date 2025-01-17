# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-权限中心(BlueKing-IAM) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from django.urls import path

from . import views

urlpatterns = [
    # -------------- 用户组本身 --------------
    # 系统管理员下创建用户组
    path(
        "grade_managers/-/groups/",
        views.ManagementSystemManagerGroupViewSet.as_view({"post": "create"}),
        name="open.management.v2.system_manager_group",
    ),
    # 分级管理员下创建用户组
    path(
        "grade_managers/<int:id>/groups/",
        views.ManagementGradeManagerGroupViewSet.as_view({"post": "create"}),
        name="open.management.v2.grade_manager_group",
    ),
    # 用户组基本信息更新 & 删除
    path(
        "groups/<int:id>/",
        views.ManagementGroupViewSet.as_view({"put": "update", "delete": "destroy"}),
        name="open.management.v2.group",
    ),
    # -------------- 用户组成员 --------------
    # 用户组成员
    path(
        "groups/<int:id>/members/",
        views.ManagementGroupMemberViewSet.as_view({"get": "list", "post": "create", "delete": "destroy"}),
        name="open.management.v2.group_member",
    ),
    # 用户组成员有效期
    path(
        "groups/<int:id>/members/-/expired_at/",
        views.ManagementGroupMemberExpiredAtViewSet.as_view({"put": "update"}),
        name="open.management.v2.group_member.expired_at",
    ),
    # -------------- 用户组权限 --------------
    # 用户组自定义权限
    path(
        "groups/<int:id>/policies/",
        views.ManagementGroupPolicyViewSet.as_view({"post": "create", "delete": "destroy"}),
        name="open.management.v2.group_policy",
    ),
    # 用户组自定义权限 - 操作级别的变更，不涉及Resources
    path(
        "groups/<int:id>/actions/-/policies/",
        views.ManagementGroupActionPolicyViewSet.as_view({"delete": "destroy"}),
        name="open.management.v2.group_action",
    ),
    path(
        "groups/<int:id>/policies/-/actions/",
        views.ManagementGroupPolicyActionViewSet.as_view({"get": "list"}),
        name="open.management.v2.group_action",
    ),
    # -------------- 申请 --------------
    # 用户组申请单
    path(
        "groups/-/applications/",
        views.ManagementGroupApplicationViewSet.as_view({"post": "create"}),
        name="open.management.v2.group_application",
    ),
    # -------------- Subject --------------
    # 用户 - 所属用户组判定
    path(
        "users/<str:user_id>/groups/belong/",
        views.ManagementUserGroupBelongViewSet.as_view({"get": "check"}),
        name="open.management.v2.user_group_belong",
    ),
    # 部门 - 所属用户组判定
    path(
        "departments/<int:id>/groups/belong/",
        views.ManagementDepartmentGroupBelongViewSet.as_view({"get": "check"}),
        name="open.management.v2.department_group_belong",
    ),
]
