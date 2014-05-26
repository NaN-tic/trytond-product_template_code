#This file is part product_template_code module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Template']
__metaclass__ = PoolMeta


class Template:
    __name__ = "product.template"
    code = fields.Function(fields.Char('Code'), 'on_change_with_code')

    @fields.depends('products')
    def on_change_with_code(self, name=None):
        code = None
        if self.products:
            code = self.products[0].code
        return code
