# -*- coding: utf-8 -*-
from odoo import http

# class O3Timings(http.Controller):
#     @http.route('/o3_timings/o3_timings/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/o3_timings/o3_timings/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('o3_timings.listing', {
#             'root': '/o3_timings/o3_timings',
#             'objects': http.request.env['o3_timings.o3_timings'].search([]),
#         })

#     @http.route('/o3_timings/o3_timings/objects/<model("o3_timings.o3_timings"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('o3_timings.object', {
#             'object': obj
#         })