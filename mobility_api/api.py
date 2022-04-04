import frappe

@frappe.whitelist()
def get_orders(filters = {}, order_by = 'transaction_date desc', start = 0, page_length = 20):
	response = []
	orders = frappe.get_list('Sales Order', filters = filters, order_by = order_by, start = start, page_length = page_length)
	for order in orders:
		order_detail = frappe.db.get_value('Sales Order', order.name, ['name', 'transaction_date', 'delivery_date', 'customer_name', 'status', 'net_total', 'total_taxes_and_charges', 'grand_total'], as_dict = 1)
		top_items = frappe.get_list('Sales Order Item', filters = {'parent': order.name}, fields = ['item_name', 'qty', 'uom', 'stock_qty', 'stock_uom', 'rate', 'amount'], order_by = 'stock_qty desc', page_length = 3)
		order_detail['items'] = top_items
		response.append(order_detail)

	return response
