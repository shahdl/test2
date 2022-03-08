from odoo import api, fields, models, _


class CreateBookWizard(models.TransientModel):
    _name = "create_book_wizard"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "create book wizard"

    name = fields.Char(string='Book Tittle', required=True)
    date = fields.Date(string='', required=True)
    writer = fields.Char(string='Writer', required=True, tracking=True)

    def action_create_book(self):
        print('create book')
        vals = {
            'name': self.name,
            'writer': self.writer,
            'date': self.date
        }
        self.env['library_management'].create(vals)
        # return {
        #     'name': _('create book'),
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'library_management',
        #     'res_id': self.employee_id.id,
        #     'name': self.employee_id.display_name,
        #     'view_mode': 'form',
        #     'views': [(False, "form")],
        # }

