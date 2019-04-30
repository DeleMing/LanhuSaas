# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555501923.236
_enable_loop = True
_template_filename = 'D:/py-workspace/LanhuSaas/framework/templates/db_connection/database.html'
_template_uri = './db_connection/database.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html>\r\n<head>\r\n <meta charset="UTF-8">\r\n    <!-- \u5f00\u53d1\u73af\u5883\u7248\u672c\uff0c\u5305\u542b\u4e86\u6709\u5e2e\u52a9\u7684\u547d\u4ee4\u884c\u8b66\u544a--2.5.51 -->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/vue.development.js"></script>\r\n    <!-- element UI\u5f15\u5165\u6837\u5f0f -->\r\n    <link rel="stylesheet" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.css">\r\n    <!-- element UI\u5f15\u5165\u7ec4\u4ef6\u5e93 -->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/element-2.4.11/index.js"></script>\r\n    <!--axios.min.js--vue.js\u7684ajax\u652f\u6301-->\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/vue-2.5.21/axios.min.js"></script>\r\n    <script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/jquery/jquery-3.1.1.min.js"></script>\r\n    <link type="text/css" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/home.css" rel="stylesheet">\r\n    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/v-charts/lib/style.min.css">\r\n</head>\r\n\r\n<body>\r\n<div class="content" id="main">\r\n    <div class="header">\r\n        <el-breadcrumb class="route" separator-class="el-icon-arrow-right">\r\n            <el-breadcrumb-item>\u9996\u9875</el-breadcrumb-item>\r\n            <el-breadcrumb-item>SQL\u6570\u636e\u5e93\u8fde\u63a5\u7ba1\u7406</el-breadcrumb-item>\r\n        </el-breadcrumb>\r\n    </div>\r\n\r\n    <div class="body">\r\n        <el-card shadow="always">\r\n            <!--\u8868\u5355\u5c55\u793a-->\r\n            <div v-if="isAdd == \'1\'">\r\n                <div id="pagetitle">\r\n                    SQL\u6570\u636e\u5e93\u8fde\u63a5\u7ba1\u7406\r\n                </div>\r\n                <hr id="hr">\r\n                <el-row type="flex" justify="space-between" align="center" class="row">\r\n\r\n                    <el-col :span="12">\r\n                        <el-col :span="9">\r\n                            <el-input v-model="search" placeholder="\u8bf7\u8f93\u5165\u5185\u5bb9"></el-input>\r\n                        </el-col>\r\n                        <el-col :span="3">\r\n                            <el-button type="primary" icon="el-icon-search" v-on:click="select_table">\u641c\u7d22</el-button>\r\n                        </el-col>\r\n                    </el-col>\r\n                <el-col :span=\'3\'>\r\n                    <el-button type=\'primary\'  @click=\'show\'>\u65b0\u589e\u6570\u636e\u5e93\u8fde\u63a5</el-button>\r\n                </el-col>\r\n                </el-row>\r\n\r\n                <el-table :data="tableData" :header-cell-style="rowClass" style="width: 100%">\r\n                    <el-table-column prop="id" label="\u5e8f\u53f7" width="80px">\r\n                    </el-table-column>\r\n                    <el-table-column prop="connname" label="\u8fde\u63a5\u540d\u79f0" style="width: 25%">\r\n                    </el-table-column>\r\n                    <el-table-column prop="type" label="\u8fde\u63a5\u7c7b\u578b" style="width: 25%">\r\n                    </el-table-column>\r\n                    <el-table-column prop="ip" label="IP\u5730\u5740" style="width: 25%">\r\n                    </el-table-column>\r\n                    <el-table-column prop="port" label="\u7aef\u53e3" style="width: 25%">\r\n                    </el-table-column>\r\n                    <el-table-column prop="username" label="\u7528\u6237\u540d" style="width: 25%">\r\n                    </el-table-column>\r\n                    <el-table-column prop="operation" label="\u64cd\u4f5c">\r\n                        <template slot-scope="scope">\r\n                            <el-button type="text" @click="showe(scope.row)" size="small">\u7f16\u8f91</el-button>\r\n                            <el-button type="text" @click="deleteDataBase(scope.row.id,scope.$index,tableData)" size="small">\u5220\u9664</el-button>\r\n                        </template>\r\n                    </el-table-column>\r\n                </el-table>\r\n                <el-pagination :page-count="page_count" background layout="prev, pager, next" style="float:right" @current-change="current_change1"></el-pagination>\r\n            </div>\r\n\r\n            <!--\u65b0\u589e-->\r\n            <div v-else-if="isAdd == \'2\'">\r\n                <div id="pagetitle">\r\n                    \u65b0\u589e\u6570\u636e\u5e93\u8fde\u63a5\r\n                </div>\r\n                <hr id="hr">\r\n                <el-form label-width="140px" :model="addconn" ref="addconn" :rules="rules" class="demo-ruleForm">\r\n                    <el-row type="flex" class="row-bg" justify="space-around">\r\n                        <el-col :span="9">\r\n                            <el-form-item label="\u8fde\u63a5\u540d\u79f0\uff1a" prop="connname">\r\n                                <el-input v-model="addconn.connname"></el-input>\r\n                            </el-form-item>\r\n                        </el-col>\r\n                        <el-col :span="9">\r\n                            <el-form-item label="\u6570\u636e\u5e93\u7c7b\u578b:" prop="type">\r\n                                    <el-select v-model="addconn.type" placeholder="\u8bf7\u9009\u62e9\u6570\u636e\u5e93\u7c7b\u578b" style="width: 250px;">\r\n                                        <el-option label="MySQL" value="MySQL"></el-option>\r\n                                        <el-option label="Oracle" value="Oracle"></el-option>\r\n                                        <el-option label="SQL Server" value="SQL Server"></el-option>\r\n                                    </el-select>\r\n                            </el-form-item>\r\n                        </el-col>\r\n                    </el-row>\r\n                    <el-row type="flex" class="row-bg" justify="space-around">\r\n                        <el-col :span="9">\r\n                            <el-form-item label="Ip\u5730\u5740\uff1a" prop="ip">\r\n                                <el-input v-model="addconn.ip"></el-input>\r\n                            </el-form-item>\r\n                        </el-col>\r\n                        <el-col :span="9">\r\n                            <el-form-item label="\u7aef\u53e3\u53f7\uff1a" prop="port">\r\n                                <el-input v-model="addconn.port"></el-input>\r\n                            </el-form-item>\r\n                        </el-col>\r\n                    </el-row>\r\n                    <el-row type="flex" class="row-bg" justify="space-around">\r\n                        <el-col :span="9">\r\n                            <div id="son">\r\n                                <el-form-item label="\u6570\u636e\u5e93\u540d\u79f0\uff1a" prop="databasename">\r\n                                    <el-input v-model="addconn.databasename"></el-input>\r\n                                </el-form-item>\r\n                            </div>\r\n                        </el-col>\r\n                        <el-col :span="9">\r\n                            <div id="son">\r\n                                <el-form-item label="\u7528\u6237\u540d\uff1a" prop="username">\r\n                                    <el-input v-model="addconn.username"></el-input>\r\n                                </el-form-item>\r\n                            </div>\r\n                        </el-col>\r\n\r\n                    </el-row>\r\n                    <el-row type="flex" class="row-bg" justify="space-around">\r\n                        <el-col :span="9">\r\n                            <div id="son">\r\n                                <el-form-item label="\u5bc6\u7801\uff1a" prop="password">\r\n                                    <el-input v-model="addconn.password" type="password"></el-input>\r\n                                </el-form-item>\r\n                            </div>\r\n                        </el-col>\r\n\r\n                    </el-row>\r\n                </el-form>\r\n                <el-row type="flex" class="row-bg" justify="center">\r\n                    <el-col :span="18">\r\n                        <el-button type="info" @click="testConn(\'addconn\')">\u6d4b\u8bd5\u8fde\u63a5</el-button>\r\n                    </el-col>\r\n                    <el-col :span="2">\r\n                        <el-button type="primary" id="button" @click="saveconn(\'addconn\')">\u4fdd\u5b58</el-button>\r\n                    </el-col>\r\n                    <el-col :span="2">\r\n                        <el-button @click="hide()" id="button">\u53d6\u6d88</el-button>\r\n                    </el-col>\r\n                </el-row>\r\n            </div>\r\n\r\n            <!--\u7f16\u8f91-->\r\n            <div v-else="isAdd == \'3\'">\r\n                <div id="pagetitle">\r\n                    \u7f16\u8f91\u6570\u636e\u5e93\u8fde\u63a5\r\n                </div>\r\n                <hr id="hr">\r\n                <el-form label-width="140px" :model="editDataBase" ref="editDataBase" :rules="rules" class="demo-ruleForm">\r\n                    <el-row type="flex" class="row-bg" justify="space-around">\r\n                        <el-col :span="9">\r\n                            <el-form-item label="\u8fde\u63a5\u540d\u79f0\uff1a" prop="connname">\r\n                                <el-input v-model="editDataBase.connname"></el-input>\r\n                            </el-form-item>\r\n                        </el-col>\r\n                        <el-col :span="9">\r\n                            <el-form-item label="\u6570\u636e\u5e93\u7c7b\u578b:" prop="type">\r\n                                    <el-select v-model="editDataBase.type" placeholder="\u8bf7\u9009\u62e9\u6570\u636e\u5e93\u7c7b\u578b" style="width: 250px;">\r\n                                        <el-option label="MySQL" value="MySQL"></el-option>\r\n                                        <el-option label="Oracle" value="Oracle"></el-option>\r\n                                        <el-option label="SQL Server" value="SQL Server"></el-option>\r\n                                    </el-select>\r\n                            </el-form-item>\r\n                        </el-col>\r\n                    </el-row>\r\n                    <el-row type="flex" class="row-bg" justify="space-around">\r\n                        <el-col :span="9">\r\n                            <el-form-item label="Ip\u5730\u5740\uff1a" prop="ip">\r\n                                <el-input v-model="editDataBase.ip"></el-input>\r\n                            </el-form-item>\r\n                        </el-col>\r\n                        <el-col :span="9">\r\n                            <el-form-item label="\u7aef\u53e3\u53f7\uff1a" prop="port">\r\n                                <el-input v-model="editDataBase.port"></el-input>\r\n                            </el-form-item>\r\n                        </el-col>\r\n                    </el-row>\r\n                    <el-row type="flex" class="row-bg" justify="space-around">\r\n                        <el-col :span="9">\r\n                            <div id="son">\r\n                                <el-form-item label="\u6570\u636e\u5e93\u540d\u79f0\uff1a" prop="databasename">\r\n                                    <el-input v-model="editDataBase.databasename"></el-input>\r\n                                </el-form-item>\r\n                            </div>\r\n                        </el-col>\r\n                        <el-col :span="9">\r\n                            <div id="son">\r\n                                <el-form-item label="\u7528\u6237\u540d\uff1a" prop="username">\r\n                                    <el-input v-model="editDataBase.username"></el-input>\r\n                                </el-form-item>\r\n                            </div>\r\n                        </el-col>\r\n\r\n                    </el-row>\r\n                    <el-row type="flex" class="row-bg" justify="space-around">\r\n                        <el-col :span="9">\r\n                            <div id="son">\r\n                                <el-form-item label="\u5bc6\u7801\uff1a" prop="password">\r\n                                    <el-input v-model="editDataBase.password" type="password"></el-input>\r\n                                </el-form-item>\r\n                            </div>\r\n                        </el-col>\r\n\r\n                    </el-row>\r\n                </el-form>\r\n                <el-row type="flex" class="row-bg" justify="center">\r\n                    <el-col :span="18">\r\n                        <el-button type="info" @click="textconn2(\'editDataBase\')">\u6d4b\u8bd5\u8fde\u63a5</el-button>\r\n                    </el-col>\r\n                    <el-col :span="2">\r\n                        <el-button type="primary" @click="editConn(\'editDataBase\')">\u4fee\u6539</el-button>\r\n                    </el-col>\r\n                    <el-col :span="2">\r\n                        <el-button @click="hide()">\u53d6\u6d88</el-button>\r\n                    </el-col>\r\n                </el-row>\r\n            </div>\r\n            <!--||||||||||||||||-->\r\n        </el-card>\r\n    </div>\r\n\r\n</div>\r\n\r\n<script type="text/javascript">\r\n    var ve = new Vue({\r\n        el: \'#main\',\r\n        data: {\r\n            search:\'\',//\u641c\u7d22\u6846\u7684\u503c\r\n            page_count:200,\r\n            page:1, //\u5f53\u524d\u9875\r\n            isAdd: 1,\r\n            tableData: [],\r\n            dataType:[],\r\n            editDataBase:[],\r\n            addconn: {\r\n                connname:\'\',\r\n                type:\'\',\r\n                ip: \'\',\r\n                port: \'\',\r\n                username:\'\',\r\n                password:\'\',\r\n                databasename:\'\',\r\n            },\r\n            rules: {\r\n                connname: [\r\n                    { required: true, message: \'\u8bf7\u8f93\u5165\u8fde\u63a5\u540d\u79f0\', trigger: \'blur\' },\r\n                    { min: 1, max: 20, message: \'\u957f\u5ea6\u5728 1 \u5230 20 \u4e2a\u5b57\u7b26\', trigger: \'blur\' },\r\n\r\n              ],\r\n                ip: [\r\n                    { required: true, message: \'\u8bf7\u8f93\u5165ip\u5730\u5740\', trigger: \'blur\' },\r\n                    {pattern: /^(\\d{1,2}|1\\d\\d|2[0-4]\\d|25[0-5])\\.(\\d{1,2}|1\\d\\d|2[0-4]\\d|25[0-5])\\.(\\d{1,2}|1\\d\\d|2[0-4]\\d|25[0-5])\\.(\\d{1,2}|1\\d\\d|2[0-4]\\d|25[0-5])$/,message:\'\u8bf7\u8f93\u5165\u6b63\u786e\u7684IP\u5730\u5740\',trigger: \'blur\' }\r\n              ],\r\n                port: [\r\n                    { required: true, message: \'\u8bf7\u8f93\u5165\u7aef\u53e3\u53f7\', trigger: \'blur\' },\r\n                    {pattern:/^([0-9]|[1-9]\\d{1,3}|[1-5]\\d{4}|6[0-4]\\d{4}|65[0-4]\\d{2}|655[0-2]\\d|6553[0-5])$/,message:\'\u8bf7\u8f93\u5165\u6b63\u786e\u7aef\u53e3\u53f7\',trigger: \'blur\' }\r\n              ],\r\n                databasename: [\r\n                { required: true, message: \'\u8bf7\u8f93\u5165\u6570\u636e\u5e93\u540d\u79f0\', trigger: \'blur\' },\r\n                { min: 1, max: 20, message: \'\u957f\u5ea6\u5728 1 \u5230 20 \u4e2a\u5b57\u7b26\', trigger: \'blur\' }\r\n              ],\r\n                type: [\r\n                { required: true, message: \'\u8bf7\u9009\u62e9\u6570\u636e\u5e93\u7c7b\u578b\', trigger: \'blur\' },\r\n              ],\r\n                username: [\r\n                    { required: true, message: \'\u8bf7\u8f93\u5165\u7528\u6237\u540d\', trigger: \'blur\' },\r\n                    { min: 1, max: 20, message: \'\u957f\u5ea6\u5728 1 \u5230 20 \u4e2a\u5b57\u7b26\', trigger: \'blur\' }\r\n              ],\r\n                password: [\r\n                    { required: true, message: \'\u8bf7\u8f93\u5165\u5bc6\u7801\', trigger: \'blur\' },\r\n                    { min: 3, max: 20, message: \'\u957f\u5ea6\u5728 3 \u5230 20 \u4e2a\u5b57\u7b26\', trigger: \'blur\' }\r\n              ]\r\n            },\r\n\r\n\r\n        },\r\n        methods: {\r\n            current_change1(value) {\r\n                ve.page = value;\r\n                ve.conn()\r\n            },\r\n            show() {\r\n                this.addconn = null\r\n                this.isAdd = 2\r\n            },\r\n\r\n            hide() {\r\n                this.isAdd=1\r\n                ve.conn()\r\n            },\r\n\r\n            rowClass({row, rowIndex}) {\r\n                return \'background:#F7F7F7\'\r\n            },\r\n\r\n\r\n            //\u641c\u7d22\r\n            select_table() {\r\n                axios({\r\n                    method: \'post\',\r\n                    url: \'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u"DataBaseManage/selecthor/',\r\n                    data: {\r\n                        search:this.search,\r\n                        page:ve.page,\r\n                        limit:5,\r\n                    }\r\n                }).then((res) => {\r\n                    ve.tableData = res.data.message;\r\n                    ve.page_count = res.data.message[0].page_count;\r\n                })\r\n            },\r\n            //\u67e5\u8be2\u6240\u6709\r\n            conn(){\r\n                 axios({\r\n                    method: 'post',\r\n                    url: '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"DataBaseManage/getall/',\r\n                    data:{\r\n                        page:ve.page,\r\n                        limit:5,\r\n                    }\r\n                }).then(function(response) {\r\n                    ve.tableData = response.data.message\r\n                    ve.page_count = response.data.message[0].page_count;\r\n                })\r\n            },\r\n\r\n\r\n\r\n            //\u4fdd\u5b58\r\n            saveconn(formName){\r\n               this.$refs[formName].validate((valid) => {\r\n                    if (!valid) {\r\n                        alert('\u9a8c\u8bc1\u4e0d\u901a\u8fc7');\r\n                        return false;\r\n                    }else {\r\n                        axios.post(\r\n                        '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"DataBaseManage/saveconn/',this.addconn\r\n                    ).then(function (res) {\r\n                        if(res.data.message == 0){\r\n                            ve.hide()\r\n                        }\r\n                    });\r\n                    }\r\n                });\r\n            },\r\n\r\n\r\n            //\u53bb\u4fee\u6539\r\n            showe(row){\r\n                this.isAdd = 3\r\n                this.editDataBase=row\r\n            },\r\n\r\n            //\u4fee\u6539\r\n            editConn(formName){\r\n                this.$refs[formName].validate((valid) => {\r\n                    if (!valid) {\r\n                        alert('\u9a8c\u8bc1\u4e0d\u901a\u8fc7');\r\n                        return false;\r\n                    }else {\r\n                        axios.post('")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"DataBaseManage/editconn/',this.editDataBase)\r\n                    .then((res)=>{\r\n                        if(res.data.message != null){\r\n                            this.isAdd = 1\r\n                            ve.conn()\r\n                        }\r\n                    })\r\n                    }\r\n                })\r\n            },\r\n\r\n\r\n            //\u5220\u9664\r\n            deleteDataBase(id,index,data){\r\n            this.$confirm('\u6b64\u64cd\u4f5c\u5c06\u6c38\u4e45\u5220\u9664\u8be5\u76d1\u63a7\u9879, \u662f\u5426\u7ee7\u7eed?', '\u63d0\u793a', {\r\n                confirmButtonText: '\u786e\u5b9a',\r\n                cancelButtonText: '\u53d6\u6d88',\r\n                type: 'warning',\r\n                center: true\r\n            }).then(() => {\r\n                this.$message({\r\n                        type: 'success',\r\n                        message: '\u5220\u9664\u6210\u529f!',\r\n                    },\r\n                    axios.post(\r\n                   '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"DataBaseManage/deleteconn/'+id+'/'\r\n               ).then((res) => {\r\n                   if(res.data.message==0){\r\n                       this.$message('\u5220\u9664\u6210\u529f')\r\n                       data.splice(index,1)\r\n                   }\r\n                    })\r\n                    ,\r\n                );\r\n            }).catch(() => {\r\n                this.$message({\r\n                    type: 'info',\r\n                    message: '\u5df2\u53d6\u6d88\u5220\u9664'\r\n                });\r\n            });\r\n        },\r\n\r\n            //\u6570\u636e\u5e93\u8fde\u63a5\u6d4b\u8bd5\r\n            testConn(formName){\r\n                console.log(this.addconn)\r\n                this.$refs[formName].validate((valid) => {\r\n                    if (!valid) {\r\n                        alert('\u9a8c\u8bc1\u4e0d\u901a\u8fc7');\r\n                        return false;\r\n                    }else {\r\n                        axios.post('")
        __M_writer(unicode(SITE_URL))
        __M_writer(u'DataBaseManage/testConn/\',this.addconn)\r\n                            .then((res)=>{\r\n                        if(res.data.message == 1){\r\n                             alert("\u6570\u636e\u5e93\u8fde\u63a5\u6210\u529f")\r\n                        }else{\r\n                            alert("\u6570\u636e\u5e93\u8fde\u63a5\u5931\u8d25")\r\n                        }\r\n                    })\r\n                    }\r\n                })\r\n\r\n            },\r\n\r\n            //\u6d4b\u8bd52\r\n            textconn2(formName){\r\n                this.$refs[formName].validate((valid) => {\r\n                    if (!valid) {\r\n                        alert(\'\u9a8c\u8bc1\u4e0d\u901a\u8fc7\');\r\n                        return false;\r\n                    }else {\r\n                        axios.post(\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'DataBaseManage/testConn/\',this.editDataBase)\r\n                            .then((res)=>{\r\n                        if(res.data.message == 1){\r\n                             alert("\u6570\u636e\u5e93\u8fde\u63a5\u6210\u529f")\r\n                        }else{\r\n                            alert("\u6570\u636e\u5e93\u8fde\u63a5\u5931\u8d25")\r\n                        }\r\n                    })\r\n                    }\r\n                })\r\n\r\n            },\r\n        }\r\n    });\r\n    ve.conn()\r\n</script>\r\n\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 6, "25": 6, "26": 8, "27": 8, "28": 10, "29": 10, "30": 12, "31": 12, "32": 13, "33": 13, "34": 14, "35": 14, "36": 307, "37": 307, "38": 322, "39": 322, "40": 343, "41": 343, "42": 367, "43": 367, "44": 392, "45": 392, "46": 417, "47": 417, "48": 437, "49": 437, "55": 49}, "uri": "./db_connection/database.html", "filename": "D:/py-workspace/LanhuSaas/framework/templates/db_connection/database.html"}
__M_END_METADATA
"""