from odoo import api, fields, models, _


class Director(models.Model):
    _name = "director"
    _description = "movie_management"

    name = fields.Char(string='Director Name', tracking=True)
    actor = fields.Char(string='Person Name', tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    nation = fields.Char(string='Nationality', required=True, tracking=True)
    job = fields.Selection([
        ('actor', 'Actor'),
        ('actress', 'Actress')
    ],  default='actor', tracking=True)
    date = fields.Date(string='Date Of Birth', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Statues", tracking=True)
    image = fields.Binary(string='Poster Image')

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
            vals['note'] = 'New Person'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('director') or _('New')
        res = super(Director, self).create(vals)
        return res
