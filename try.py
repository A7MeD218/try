def add_to_cart():
    quantity_value = int(quantity_e.get())
    if quantity_value > int(get_stock):
        tkinter.messagebox.showinfo("Error", "Not that any products in our stock.")
    else:
        # calculate the price first
        final_price = (float(quantity_value) * float(get_price)) - (float(discount_e.get()))
        products_list.append(get_name)
        product_price.append(final_price)
        product_quantity.append(quantity_value)
        product_id.append(get_id)

        x_index = 0
        y_index = 100
        counter = 0
        for p in products_list:
            tempname = Label(right, text=str(products_list[counter]), font=('arial', 18, 'bold'),
                             bg='Light blue', fg='white')
            tempname.place(x=0, y=y_index)
            tempqt = Label(right, text=str(product_quantity[counter]), font=('arial', 18, 'bold'),
                           bg='Light blue', fg='white')
            tempqt.place(x=300, y=y_index)
            tempprice = Label(right, text=str(product_price[counter]), font=('arial', 18, 'bold'),
                              bg='Light blue', fg='white')
            tempprice.place(x=500, y=y_index)

            y_index += 40
            counter += 1
