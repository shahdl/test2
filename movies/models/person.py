from odoo import api, fields, models, _


class Person(models.Model):
    _name = "person"
    _description = "person_management"

    name = fields.Char(string='Actor Name', tracking=True)
    director = fields.Char(string='Director Name', tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    nation = fields.Char(string='Nationality', required=True, tracking=True)
    job = fields.Selection([
        ('actor', 'Actor'),
        ('actress', 'Actress'),
        ('director', 'Director')
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
            vals['reference'] = self.env['ir.sequence'].next_by_code('person') or _('New')
        res = super(Person, self).create(vals)
        return res
