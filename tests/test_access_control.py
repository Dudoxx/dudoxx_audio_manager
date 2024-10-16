from odoo.tests import TransactionCase

class TestAccessControl(TransactionCase):

    def setUp(self):
        super(TestAccessControl, self).setUp()
        self.AccessControl = self.env['dudoxx.audio.access.control']

    def test_create_access_control(self):
        access_control = self.AccessControl.create({
            'name': 'Test Access Control',
            'model_id': self.env.ref('dudoxx.audio.recording').id,
            'group_id': self.env.ref('base.group_user').id,
            'permission_type': 'read',
        })
        self.assertEqual(access_control.name, 'Test Access Control')
        self.assertEqual(access_control.permission_type, 'read')
