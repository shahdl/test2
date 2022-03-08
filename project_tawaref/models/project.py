from odoo import api, fields, models, _


class TProject(models.Model):
    _name = 'tproject'
    # _inherit = 'project.project'

    startup = fields.Char(string="the Name of the Startup")
