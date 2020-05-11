# coding=utf-8

import xlrd
import json
import codecs


class excel_read:
    def __init__(self, excel_path=r'D:\\工作\\项目文件\\C11项目资料\\C11微前端应用组合\\模块数据—韩中\\油气销售-工业APP.xlsx', encoding='utf-8', index=0):

        self.data = xlrd.open_workbook(excel_path)  # 获取文本对象
        self.table = self.data.sheets()[index]  # 根据index获取某个sheet
        self.rows = self.table.nrows  # 3获取当前sheet页面的总行数,把每一行数据作为list放到 list

    def get_data(self):
        result = []
        type = ['生产类', '管理类', '服务类']
        tag = ['工业APP', '云化软件']
        for i in range(self.rows):
            col = self.table.row_values(i)  # 获取每一列数据
            # 工业APP tag[0]        云化软件tag[1]
            if col[1] == type[0] and col[2] == tag[0]:
                excel_dict = {}
                excel_dict['type'] = col[1]
                excel_dict['tag'] = col[2]
                excel_dict['name'] = col[3]
                excel_dict['intro'] = col[4]
                # item = {'type': col[1], 'tag': col[2],
                # 'name': col[3], 'intro': col[4]}
                result.append(excel_dict)
        excel_json = json.dumps(result, ensure_ascii=False)
        print(result, len(result))
        with codecs.open('D:\\工作\\项目文件\\工业互联网平台官网\\微前端导航栏项目\\riip-micro-frontend\\src\\redux\\actions\\app_info\\app_info_8.json', "w", "utf-8") as f:
            f.write(excel_json)
        return excel_json


if __name__ == '__main__':
    excel_read().get_data()
