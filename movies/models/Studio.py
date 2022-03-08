from odoo import api, fields, models, _


class Studio(models.Model):
    _name = "studio"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "studio_management"

    name = fields.Char(string='Studio Name', tracking=True)
    country = fields.Char(string='Country ', tracking=True)
    reference = fields.Char(string='Order Reference', copy=False, readonly=True, default=lambda self: _('New'))
    date = fields.Date(string='Establishment Year')
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Statues", tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Respnsible")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Director'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('studio') or _('New')
        res = super(Studio, self).create(vals)
        return res
