from odoo import api, fields, models, _


class Genres(models.Model):
    _name = "genres"
    _description = "movie_management"

    genre = fields.Char(string='Genres', tracking=True)

    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))

    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Statues", tracking=True)
    image = fields.Binary(string='Poster Image')

    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': 'http://0.0.0.0:8099/web#action=86&model=person&view_type=list&cids=&menu_id=69'
        }

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, rec.genre))
            # res.append((record.id, record.genre))
        return res

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Genres'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('genres') or _('New')
        res = super(Genres, self).create(vals)
        return res
