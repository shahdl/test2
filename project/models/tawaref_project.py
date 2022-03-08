from .project import ProjectTaskType
from odoo import api, fields, models, _


class TawarefProject(models.Model):
    _inherit = 'project.project'

    deal_manager = fields.Many2many('res.users', string='Deal Manager')
    deal_admin = fields.Many2one('res.users', string='Deal Admin')
    deal_date = fields.Date()
    scout = fields.Char()
    dds = fields.Many2one('res.users', string='DDS')
    contact = fields.Char(string='Phone/Email')
    tawaref_admin = fields.Char()

    @api.model
    def default_get(self, fields):
        res = super(TawarefProject, self).default_get(fields)
        res['scout'] = 'Tawaref'
        return res

    @api.model
    def create(self, vals_list):
        deal = super().create(vals_list)
        print(deal, deal.id)

        stage1 = self.env['project.task.type'].create({'project_ids': [deal.id, ], 'name': 'DD Deal '})
        print(stage1)
        task1 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Scout Invited the Startup'})
        task2 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Lead DD Assigned '})
        task3 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'DD Approved the Pitch'})
        task4 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Startup Onboarded'})
        task2 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Lead DD Chose other DD'})
        task2 = self.env['project.task'].create({'stage_id': stage1.id, 'project_id': deal.id, 'name': 'DD Meeting 1'})
        task2 = self.env['project.task'].create({'stage_id': stage1.id, 'project_id': deal.id, 'name': 'DD Meeting 2'})
        task2 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Sent Requested Files'})
        task2 = self.env['project.task'].create({'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Memo Drafted'})
        task2 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'DD Consilidation Meeting'})
        task2 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Lead DD Accepted'})
        task2 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Tawaref Accepted '})
        task2 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Memo sent to Scout '})
        task2 = self.env['project.task'].create(
            {'stage_id': stage1.id, 'project_id': deal.id, 'name': 'Scout Debriefed'})

        raising = self.env['project.task.type'].create({'project_ids': [deal.id, ], 'name': 'Raising'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Confirmation Email '})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Tawaref FeeDeposited '})
        task1 = self.env['project.task'].create({'stage_id': raising.id, 'project_id': deal.id, 'name': 'KYC DocsSent'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Fee/KYC AutoEmail Sent'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Investor Comitted/Rejected'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Follow Up Message Sent'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Investor Only Session'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'PitchConducted'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Same DayReminder'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Pitch Invitation is Sent '})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Founder Invited Investors'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Investors Profile Identified'})
        task1 = self.env['project.task'].create(
            {'stage_id': raising.id, 'project_id': deal.id, 'name': 'Founder Built Full Profile'})

        contracting = self.env['project.task.type'].create({'project_ids': [deal.id, ], 'name': 'Contracting '})
        task2 = self.env['project.task'].create({'stage_id': contracting.id, 'project_id': deal.id,
                                                 'name': 'Request the difference email to the investors (Deal Admin)'})
        task2 = self.env['project.task'].create(
            {'stage_id': contracting.id, 'project_id': deal.id, 'name': 'Reference  Letter Received '})
        task2 = self.env['project.task'].create({'stage_id': contracting.id, 'project_id': deal.id,
                                                 'name': 'Reference Letter/Passport Attestation request Email Sent'})
        task2 = self.env['project.task'].create({'stage_id': contracting.id, 'project_id': deal.id,
                                                 'name': 'Amount receiving confirmation on the patform (Deal Admin)'})
        task2 = self.env['project.task'].create({'stage_id': contracting.id, 'project_id': deal.id,
                                                 'name': 'Confrimation email of the amount + receipt  from the Sartup '})
        task2 = self.env['project.task'].create({'stage_id': contracting.id, 'project_id': deal.id,
                                                 'name': 'Deployment Receival Confirmed by Email (Startup)'})
        task2 = self.env['project.task'].create({'stage_id': contracting.id, 'project_id': deal.id,
                                                 'name': 'Deployed Receipt Uploaded in the System (Investor/Deal Admin)'})
        task2 = self.env['project.task'].create(
            {'stage_id': contracting.id, 'project_id': deal.id, 'name': 'Deployment Request Email Sent (Tawaref)'})
        task2 = self.env['project.task'].create({'stage_id': contracting.id, 'project_id': deal.id,
                                                 'name': 'Tawaref Signed Investment Agreemnet with the Startup'})
        task2 = self.env['project.task'].create(
            {'stage_id': contracting.id, 'project_id': deal.id, 'name': 'Subscription Agreement signed (Investor)'})
        task2 = self.env['project.task'].create(
            {'stage_id': contracting.id, 'project_id': deal.id, 'name': 'Digital Signature link Sent (Tawaref)'})
        task2 = self.env['project.task'].create(
            {'stage_id': contracting.id, 'project_id': deal.id, 'name': 'Information Confimed by investor '})
        task2 = self.env['project.task'].create(
            {'stage_id': contracting.id, 'project_id': deal.id, 'name': 'Contract Review Email Sent '})
        task2 = self.env['project.task'].create(
            {'stage_id': contracting.id, 'project_id': deal.id, 'name': 'Subscription agreement Prepared'})
        task2 = self.env['project.task'].create(
            {'stage_id': contracting.id, 'project_id': deal.id, 'name': 'Cell Constituation Prepared '})
        task2 = self.env['project.task'].create(
            {'stage_id': contracting.id, 'project_id': deal.id, 'name': 'Cell Name Selected '})

        establishment= self.env['project.task.type'].create({'project_ids': [deal.id, ], 'name': 'Establishment'})
        task2 = self.env['project.task'].create({'stage_id': establishment.id, 'project_id': deal.id, 'name': 'Auto Email Sent to the Investors '})
        task2 = self.env['project.task'].create({'stage_id': establishment.id, 'project_id': deal.id, 'name': 'Shareholder Certificates Uploaded in the System'})
        task2 = self.env['project.task'].create({'stage_id': establishment.id, 'project_id': deal.id, 'name': 'Shareholder Certificates Shared by Triadent '})
        task2 = self.env['project.task'].create({'stage_id': establishment.id, 'project_id': deal.id, 'name': 'Cell Established '})
        task2 = self.env['project.task'].create({'stage_id': establishment.id, 'project_id': deal.id, 'name': 'Cell/Stackholder Registration Fee paid'})
        task2 = self.env['project.task'].create({'stage_id': establishment.id, 'project_id': deal.id, 'name': 'KYC Fee Paid150/Investor'})
        task2 = self.env['project.task'].create({'stage_id': establishment.id, 'project_id': deal.id, 'name': 'KYC Approved '})
        task2 = self.env['project.task'].create({'stage_id': establishment.id, 'project_id': deal.id, 'name': 'All KYC Docs and Agreements Sent to Triadent '})

        return deal


