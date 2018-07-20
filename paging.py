#!/usr/bin/env python
# -*-coding:UTF-8 -*-

class Paging(object):
    def __init__(self, page_num, page_data, total_num, per_page_num=10, max_show=11):
        '''


        :param page_num: 当前页面数
        :param page_data: 页面展示数据
        :param total_num: 总数据量
        :param per_page_num: 每页数据条数
        :param max_show: 最多显示按钮
        '''

        self.page_num = page_num
        self.page_data = page_data
        self.total_num = total_num
        self.per_page_num = per_page_num
        self.max_show = max_show
        self.total_page, self.more = divmod(self.total_num, per_page_num)



    @property
    def start(self):
        return (self.page_num - 1) * self.per_page_num

    @property
    def end(self):
        return self.page_num * self.per_page_num

    @property
    def page_html(self):



        if self.more:
            self.total_page += 1
        if self.page_num > self.total_page:
            self.page_num = self.total_page
        elif self.page_num < 1:
            self.page_num = 1

        max_show = 11
        half_show = max_show // 2
        self.per_page_num = 10

        page_start = self.page_num - half_show
        page_end = self.page_num + half_show + 1

        if self.page_num + half_show >= self.total_page:
            page_end = self.total_page + 1
            page_start = self.total_page - max_show + 1
        elif self.page_num <= half_show:
            page_start = 1
            page_end = max_show + 1

        page_num_list = []

        # 添加首页
        page_num_list.append('<li><a href="/index/?page={0}">首页</a></li>'.format(1))
        # 添加上一页
        pre_page_num = self.page_num - 1
        if pre_page_num < 1:
            page_num_list.append('<li class="disabled"><a href="/index/?page={0}">上一页</a></li>'.format(pre_page_num))
        else:
            page_num_list.append('<li><a href="/index/?page={0}">上一页</a></li>'.format(pre_page_num))

        for i in range(page_start, page_end):
            if i == self.page_num:
                page_num_list.append('<li class="active"><a href="/index/?page={0}">{0}</a></li>'.format(i))
            else:
                page_num_list.append('<li><a href="/index/?page={0}">{0}</a></li>'.format(i))
        # 添加下一页
        next_page_num = self.page_num + 1
        if next_page_num > self.total_page:
            page_num_list.append('<li class="disabled"><a href="/index/?page={0}">下一页</a></li>'.format(next_page_num))
        else:
            page_num_list.append('<li><a href="/index/?page={0}">下一页</a></li>'.format(next_page_num))

        # 添加尾页
        page_num_list.append('<li><a href="/index/?page={0}">尾页</a></li>'.format(self.total_page))

        page_html = ''.join(page_num_list)

        return page_html
