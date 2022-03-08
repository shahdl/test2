from odoo import api, fields, models, _


# class ProjectInherit(models.Model):
#     _inherit = 'project.project'
#     # date = fields.Date()
#     # scout = fields.Char()
#     # dds = fields.Char()
#     # contact = fields.Char(string='Phone/Email')
#     tadmin = fields.Char(string='Tawaref admin')


class Movie(models.Model):
    _name = "movie"
    _description = "movie_management"

    title = fields.Char(string='Movie Name')
    director = fields.Many2many("person", string='Director Name', relation='movie_director')
    actor = fields.Many2many("person", string='Actor and Actress', relation='movie_actor')
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    studio = fields.Char(string='Studio')
    date = fields.Date(string='Production Year')
    genres = fields.Many2many("genres", string="Genres")
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Statues")
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
            vals['note'] = 'New Movie'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('movie') or _('New')
        res = super(Movie, self).create(vals)
        return res
