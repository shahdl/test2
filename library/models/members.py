from odoo import api, fields, models, _


class Members(models.Model):
    _name = "library.member"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Library Members"

    name = fields.Char(string='Name', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    address = fields.Char(string='Address', required=True, tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    phone = fields.Integer(string='Phone', required=True, tracking=True)
    age = fields.Integer(string='Age', required=True, tracking=True)
    date = fields.Date(string="Date of Join")
    gender = fields.Selection([
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other')
    ], required=True, default='Male', tracking=True)
    note = fields.Text(string='Note')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Statues", tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Respnsible")
    image = fields.Binary(string='Member Image')

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
            vals['note'] = 'New Book'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('library.member') or _('New')
        res = super(Members, self).create(vals)
        return res


