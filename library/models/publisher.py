from odoo import api, fields, models, _


class LibraryPublisher(models.Model):
    _name = "library_publisher"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Library Publisher"

    name_id = fields.Many2one('library_management', string='name')
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    pages = fields.Integer(string='Number of Pages', required=True, tracking=True)
    # writer_id = fields.Many2one('library_management', string='Writer')
    age = fields.Integer(string='Age', required=True, tracking=True)
    gender = fields.Selection([
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other')
    ], required=True, default='Male', tracking=True)

    categories = fields.Selection([
        ('Applied Research', 'applied research'),
        ('Basic Research', 'basic research'), ('Experimental Research', 'Experimental Research'), ('Historical Research', 'historical research'),
        ('Scientific Researches', 'scientific researches'), ('Other', 'other')
    ], required=True, default='Romance', tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Statues", tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Respnsible")
    date_publisher = fields.Date(string="Date")
    image = fields.Binary(string='Book Image')

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
            vals['reference'] = self.env['ir.sequence'].next_by_code('library.Publisher') or _('New')
        res = super(LibraryPublisher, self).create(vals)
        return res
