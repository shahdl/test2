from odoo import api, fields, models, _


class Actors(models.Model):
    _name = "actor"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "movie_management"

    name = fields.Char(string='Actor', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, default='male', tracking=True)

    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))

    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Statues", tracking=True)
    # responsible_id = fields.Many2one('res.partner', string="Respnsible")
    image = fields.Binary(string='Actor Image')

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
            vals['note'] = 'New Actor'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('actor') or _('New')
        res = super(Actors, self).create(vals)
        return res
