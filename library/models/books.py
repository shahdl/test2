from odoo import api, fields, models, _


class LibraryManagement(models.Model):
    _name = "library_management"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "library management"

    name = fields.Many2one('writer', string='name')
    publish = fields.Many2one('publish', string='publish')
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    pages = fields.Integer(string='Number of Pages',  tracking=True)
    writer = fields.Char(string='Writer', required=True, tracking=True)
    date = fields.Date(string='', required=True)
    # book_count = fields.Integer(string='Books Count', compute='_compute_book_count')
    # price = fields.Integer(string='Price', required=True, tracking=True)
    categories = fields.Selection([
        ('Romance', 'romance'),
        ('Horror', 'horror'), ('Action and adventure', 'action and adventure'), ('Science', 'science'), ('Travel', 'travel'), ('History', 'history'),
        ('Crime Thriller', 'crime thriller'), ('Drama', 'drama'), ('Scientific Researches', 'scientific researches')
    ], required=True, default='Romance', tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Statues", tracking=True)
    responsible_id = fields.Many2one('res.partner', string="Respnsible")
    image = fields.Binary(string='Book Image')

    # def _compute_book_count(self):
    #     book_count = self.env['library_management'].search_count([('writer_id', '=', self.writer_id.id)])
    #     self.book_count = book_count

    # @api.model
    # def default_get(self, fields):
    #     result = super(LibraryManagement, self).default_get(fields)
    #     return result

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
            vals['reference'] = self.env['ir.sequence'].next_by_code('library.book') or _('New')
        res = super(LibraryManagement, self).create(vals)
        return res
