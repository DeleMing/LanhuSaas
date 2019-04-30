# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555586697.71
_enable_loop = True
_template_filename = 'D:/py-workspace/LanhuSaas/framework/templates/system_config/scene_type.html'
_template_uri = './system_config/scene_type.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html lang="en" style="height: 100%">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <title>\u573a\u666f\u5206\u7ec4</title>\r\n\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/vue.development.js"></script>\r\n    <!-- \u751f\u4ea7\u73af\u5883\u7248\u672c\uff0c\u4f18\u5316\u4e86\u5c3a\u5bf8\u548c\u901f\u5ea6 \u529f\u80fd\u5b8c\u5584\u540e\u8bf7\u5c06vue.development.js\u8be5\u4e3avue.js-->\r\n    <!--<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/vue.js"></script>-->\r\n    <!-- vue\u7684ajax\u4f9d\u8d56-->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/axios.min.js"></script>\r\n    <!-- element UI\u5f15\u5165\u6837\u5f0f -->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.css" rel="stylesheet">\r\n    <!-- element UI\u5f15\u5165\u7ec4\u4ef6\u5e93 -->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.js"></script>\r\n    <script src=\'')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u"js/jquery.min.js'></script>\r\n    <script src='")
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-ui.js\'></script>\r\n    <!--jQuery\u5e93\u4f7f\u7528\u65f6\u8bf7\u4f7f\u7528\u6807\u51c6jQuery\u8bed\u6cd5-->\r\n    <!--<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/jquery/jquery-3.1.1.min.js"></script>-->\r\n    <!--\u9875\u9762\u521d\u59cb\u5316css(Tencent)-->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/init.css" rel="stylesheet">\r\n\r\n</head>\r\n<body style="height: 100%">\r\n<div id="app" style="height: 100%;">\r\n    <!--start \u9762\u5305\u5c51-->\r\n    <el-breadcrumb separator-class="el-icon-arrow-right" separator="/" style="padding: 20px;">\r\n        <el-breadcrumb-item><a href="/">\u7cfb\u7edf\u914d\u7f6e</a></el-breadcrumb-item>\r\n        <el-breadcrumb-item>\u573a\u666f\u5206\u7ec4\u914d\u7f6e</el-breadcrumb-item>\r\n    </el-breadcrumb>\r\n    <!--end \u9762\u5305\u5c51-->\r\n\r\n    <!--start \u5361\u7247 \u5217\u8868\u9875-->\r\n    <el-card class="box-card" style="margin: 20px;" style="height: 100%">\r\n        <div slot="header" class="clearfix">\r\n            <div class="grid-content bg-purple"><h2>\u573a\u666f\u5206\u7ec4\u914d\u7f6e</h2></div>\r\n            <br>\r\n            <el-row :gutter="20">\r\n                <el-col :span="20">\r\n                    <el-form :inline="true" class="demo-form-inline">\r\n                        <el-form-item label="\u573a\u666f\u5206\u7ec4\u540d\u79f0\uff1a">\r\n                            <el-input placeholder="\u8bf7\u8f93\u5165\u573a\u666f\u5206\u7ec4\u540d\u79f0" v-model="query_name"></el-input>\r\n                        </el-form-item>\r\n                        <el-form-item>\r\n                            <el-button type="primary" @click="query_scene_type">\u67e5\u8be2</el-button>\r\n                        </el-form-item>\r\n\r\n                    </el-form>\r\n                </el-col>\r\n                <el-col :span="4" style="float: right">\r\n                    <div class="grid-content bg-purple">\r\n                        <el-button type="primary" @click="add_scene_type_diaLog">\u65b0\u589e\u573a\u666f\u5206\u7ec4\u4fe1\u606f</el-button>\r\n                    </div>\r\n                </el-col>\r\n            </el-row>\r\n        </div>\r\n        <template>\r\n            <el-table\r\n                    :data="tableData"\r\n                    stripe\r\n                    style="width: 100%">\r\n                <el-table-column\r\n                        prop="id"\r\n                        label="ID"\r\n                        width="180">\r\n                </el-table-column>\r\n                <el-table-column\r\n                        prop="scene_type_name"\r\n                        label="\u573a\u666f\u7c7b\u578b\u540d\u79f0"\r\n                        width="180">\r\n                </el-table-column>\r\n                <el-table-column\r\n                        prop="create_user"\r\n                        label="\u521b\u5efa\u4eba">\r\n                </el-table-column>\r\n                <el-table-column\r\n                        prop="create_time"\r\n                        label="\u521b\u5efa\u65f6\u95f4">\r\n                </el-table-column>\r\n                <el-table-column\r\n                        prop="update_user"\r\n                        label="\u6700\u540e\u4fee\u6539\u4eba">\r\n                </el-table-column>\r\n                <el-table-column\r\n                        prop="update_time"\r\n                        label="\u6700\u540e\u4fee\u6539\u65f6\u95f4">\r\n                </el-table-column>\r\n                <el-table-column label="\u64cd\u4f5c">\r\n                    <template slot-scope="scope">\r\n                        <el-button size="mini" type="text"\r\n                                   v-on:click="edit_scene_type_by_uuid(scope.row.scene_type_id,scope.row.scene_type_name\r\n                                   ,scope.row.start_time,scope.row.stop_time)">\r\n                            \u7f16\u8f91\r\n                        </el-button>\r\n                        <el-button size="mini" type="text" v-on:click="delete_scene_by_uuid(scope.row.scene_type_id)">\r\n                            \u5220\u9664\r\n                        </el-button>\r\n                        </el-tooltip>\r\n                    </template>\r\n                </el-table-column>\r\n            </el-table>\r\n\r\n            <el-pagination :page-count="page_count" background layout="sizes, prev, pager, next" style="float:right"\r\n                           @current-change="changePage"  @size-change="changeSize" :page-sizes="[5, 10, 20, 50]" :page-size="5"></el-pagination>\r\n\r\n        </template>\r\n\r\n    </el-card>\r\n    <!--end \u5361\u7247 \u5217\u8868\u9875-->\r\n    <el-dialog title="\u65b0\u589e\u573a\u666f\u5206\u7ec4" :visible.sync="dialogFormVisible">\r\n        <el-form>\r\n            <el-form-item label="\u573a\u666f\u5206\u7ec4\u540d\u79f0">\r\n                <el-input v-model="form.name"></el-input>\r\n            </el-form-item>\r\n             <el-form-item label="\u65f6\u95f4\u8303\u56f4\u9009\u62e9">\r\n                <br>\r\n                <el-time-picker style="width: 30%" v-model="form.start_time"\r\n                                placeholder="\u5f00\u59cb\u65f6\u95f4\u70b9" format="HH:mm" value-format="HH:mm">\r\n                </el-time-picker>-----\r\n                <el-time-picker style="width: 30%" v-model="form.stop_time"\r\n                                placeholder="\u7ed3\u675f\u65f6\u95f4\u70b9" format="HH:mm" value-format="HH:mm">\r\n                </el-time-picker>\r\n            </el-form-item>\r\n        </el-form>\r\n        <div slot="footer" class="dialog-footer">\r\n            <el-button @click="dialogFormVisible = false">\u53d6 \u6d88</el-button>\r\n            <el-button type="primary" @click="add_scene_type">\u786e \u5b9a</el-button>\r\n        </div>\r\n    </el-dialog>\r\n    <el-dialog title="\u4fee\u6539\u573a\u666f\u5206\u7ec4\u540d\u79f0" :visible.sync="dialogFormVisible_edit">\r\n        <el-form>\r\n            <el-form-item label="\u573a\u666f\u5206\u7ec4\u540d\u79f0">\r\n                <el-input v-model="form.name"></el-input>\r\n            </el-form-item>\r\n\r\n            <el-form-item label="\u65f6\u95f4\u8303\u56f4\u9009\u62e9">\r\n                <br>\r\n                <el-time-picker style="width: 30%" v-model="form.start_time"\r\n                                placeholder="\u5f00\u59cb\u65f6\u95f4\u70b9" format="HH:mm" value-format="HH:mm">\r\n                </el-time-picker>-----\r\n                <el-time-picker style="width: 30%" v-model="form.stop_time"\r\n                                placeholder="\u7ed3\u675f\u65f6\u95f4\u70b9" format="HH:mm" value-format="HH:mm">\r\n                </el-time-picker>\r\n            </el-form-item>\r\n        </el-form>\r\n        <div slot="footer" class="dialog-footer">\r\n            <el-button @click="dialogFormVisible_edit = false">\u53d6 \u6d88</el-button>\r\n            <el-button type="primary" @click="edit_scene_type">\u786e \u5b9a</el-button>\r\n        </div>\r\n    </el-dialog>\r\n</div>\r\n\r\n\r\n<script>\r\n    //csrf\u9a8c\u8bc1\r\n    axios.interceptors.request.use((config) => {\r\n        config.headers[\'X-Requested-With\'] = \'XMLHttpRequest\';\r\n        let regex = /.*csrftoken=([^;.]*).*$/; // \u7528\u4e8e\u4ececookie\u4e2d\u5339\u914d csrftoken\u503c\r\n        config.headers[\'X-CSRFToken\'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];\r\n        return config\r\n    });\r\n\r\n    let vm = new Vue({\r\n        el: \'#app\',\r\n        data: {\r\n            showDiaLog: true,\r\n            tableData: [],\r\n            dialogFormVisible: false,\r\n            dialogFormVisible_edit: false,\r\n            form: {\r\n                name: \'\',\r\n                uuid: \'\',\r\n                start_time:\'\',\r\n                stop_time:\'\',\r\n            },\r\n            query_name: \'\',\r\n            page: 1,\r\n            page_count: 1,\r\n            limit:5,\r\n        },\r\n        methods: {\r\n            changeSize(value){\r\n                vm.limit = value;\r\n                vm.get_scene_type();\r\n            },\r\n            add_scene_type_diaLog(){\r\n                vm.dialogFormVisible = true;\r\n                vm.form.uuid = \'\';\r\n                vm.start_time = \'\';\r\n                vm.stop_time = \'\';\r\n                vm.name = \'\';\r\n            },\r\n            changePage(value) {\r\n                vm.page = value;\r\n                vm.get_scene_type();\r\n            },\r\n            get_scene_type() {\r\n                axios({\r\n                    url: \'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u"system_config/get_scene_type/',\r\n                    method: 'post',\r\n                    data: {'query_name': vm.query_name, page: vm.page, limit: vm.limit}\r\n                }).then((res) => {\r\n                    console.log(res);\r\n                    if (res.data.results.length != 0) {\r\n                        vm.tableData = res.data.results;\r\n                        vm.page_count = res.data.results[0]['page_count']\r\n                    }\r\n                }).catch((res) => {\r\n                    console.log(res)\r\n                })\r\n            },\r\n            delete_scene_by_uuid(uuid) {\r\n                console.log(uuid);\r\n                this.$confirm('\u6b64\u64cd\u4f5c\u5c06\u6c38\u4e45\u5220\u9664\u8be5\u6587\u4ef6, \u662f\u5426\u7ee7\u7eed?', '\u63d0\u793a', {\r\n                    confirmButtonText: '\u786e\u5b9a',\r\n                    cancelButtonText: '\u53d6\u6d88',\r\n                    type: 'warning',\r\n                    center: true\r\n                }).then(() => {\r\n                    axios({\r\n                        url: '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"system_config/delete_scene_by_uuid/',\r\n                        method: 'post',\r\n                        data: {'uuid': uuid}\r\n                    }).then((res) => {\r\n                        console.log(uuid);\r\n                        console.log(res.data.code);\r\n                        if (res.data.code == 0) {\r\n                            vm.$message.info('\u5220\u9664\u6210\u529f');\r\n                            vm.get_scene_type();\r\n                        } else {\r\n                            vm.$message.error('\u5220\u9664\u5931\u8d25');\r\n                        }\r\n                    }).catch((res) => {\r\n                        vm.$message.error('\u5220\u9664\u5931\u8d25');\r\n                        console.log(res);\r\n                    })\r\n                }).catch(() => {\r\n                    this.$message({\r\n                        type: 'info',\r\n                        message: '\u5df2\u53d6\u6d88\u5220\u9664'\r\n                    });\r\n                });\r\n\r\n            },\r\n            edit_scene_type_by_uuid(uuid, scene_type_name, start_time, stop_time) {\r\n                vm.dialogFormVisible_edit = true;\r\n                vm.form.name = scene_type_name;\r\n                vm.form.uuid = uuid;\r\n                vm.form.start_time = start_time;\r\n                vm.form.stop_time = stop_time;\r\n\r\n            },\r\n            add_scene_type() {\r\n                axios({\r\n                    url: '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"system_config/add_scene_type/',\r\n                    method: 'post',\r\n                    data: vm.form,\r\n                }).then((res) => {\r\n                    console.log(vm.form)\r\n                    console.log(res);\r\n                    if (res.data.code == 0) {\r\n                        vm.$message.info('\u65b0\u589e\u573a\u666f\u7c7b\u578b\u6210\u529f');\r\n                        vm.get_scene_type();\r\n                        vm.dialogFormVisible = false;\r\n                        vm.form.name = '';\r\n                    } else {\r\n                        vm.$message.error('\u65b0\u589e\u573a\u666f\u7c7b\u578b\u5931\u8d25' + res.data.message)\r\n                    }\r\n                }).catch((res) => {\r\n                    console.log(res);\r\n                    vm.$message.error('\u8bf7\u6c42\u9519\u8bef\uff0c\u65b0\u589e\u573a\u666f\u7c7b\u578b\u5931\u8d25')\r\n                })\r\n            },\r\n            edit_scene_type() {\r\n                axios({\r\n                    url: '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"system_config/edit_scene_type_by_uuid/',\r\n                    method: 'post',\r\n                    data: {name: vm.form.name, uuid: vm.form.uuid, start_time: vm.form.start_time, stop_time: vm.form.stop_time}\r\n                }).then((res) => {\r\n                    console.log(res);\r\n                    if (res.data.code == 0) {\r\n                        vm.$message.info('\u4fee\u6539\u6210\u529f');\r\n                        vm.get_scene_type();\r\n                        vm.dialogFormVisible_edit = false;\r\n                    } else {\r\n                        vm.$message.error('\u4fee\u6539\u5931\u8d25' + res.data.message)\r\n                    }\r\n                }).catch((res) => {\r\n                    vm.$message.error('\u5220\u9664\u5931\u8d25' + res);\r\n                    console.log(res);\r\n                })\r\n            },\r\n            query_scene_type() {\r\n                axios({\r\n                    url: '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"system_config/get_scene_type/',\r\n                    method: 'post',\r\n                    data: {query_name: vm.query_name, page: 1, limit: vm.limit}\r\n                }).then((res) => {\r\n                    console.log(res);\r\n                    vm.tableData = res.data.results;\r\n                    vm.page_count = res.data.results[0]['page_count']\r\n                }).catch((res) => {\r\n                    console.log(res)\r\n                })\r\n            }\r\n        }\r\n    });\r\n    vm.get_scene_type();\r\n</script>\r\n</body>\r\n</html>")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 7, "25": 7, "26": 9, "27": 9, "28": 11, "29": 11, "30": 13, "31": 13, "32": 15, "33": 15, "34": 16, "35": 16, "36": 17, "37": 17, "38": 19, "39": 19, "40": 21, "41": 21, "42": 199, "43": 199, "44": 221, "45": 221, "46": 255, "47": 255, "48": 276, "49": 276, "50": 295, "51": 295, "57": 51}, "uri": "./system_config/scene_type.html", "filename": "D:/py-workspace/LanhuSaas/framework/templates/system_config/scene_type.html"}
__M_END_METADATA
"""