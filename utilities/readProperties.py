import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseURL')

    @staticmethod
    def getFirstname():
        return config.get('common info', 'firstname')

    @staticmethod
    def getLastname():
        return config.get('common info', 'lastname')

    @staticmethod
    def getEmail():
        return config.get('common info', 'email')

    @staticmethod
    def getAddress1():
        return config.get('common info', 'address1')

    @staticmethod
    def getCity():
        return config.get('common info', 'city')

    @staticmethod
    def getCountry():
        return config.get('common info', 'country_name')

    @staticmethod
    def getState():
        return config.get('common info', 'state_name')

    @staticmethod
    def getZipcode():
        return config.get('common info', 'zipcode')

    @staticmethod
    def getLoginname():
        return config.get('common info', 'login_name')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')

    @staticmethod
    def getConfirmPassword():
        return config.get('common info', 'confirm_password')

    @staticmethod
    def getLoginURL():
        return config.get('common info', 'loginURL')

    @staticmethod
    def getLoginId():
        return config.get('common info', 'login_id')

    @staticmethod
    def getLoginPassword():
        return config.get('common info', 'login_password')

    @staticmethod
    def getHomepageURL():
        return config.get('common info', 'homepage_url')

    @staticmethod
    def getproductlink():
        return config.get('common info', 'product_link')

    @staticmethod
    def getmenu():
        return config.get('common info', 'menu_link')

    @staticmethod
    def getorderhistory():
        return config.get('common info', 'orderhistory_link')

    @staticmethod
    def getfacebooklink():
        return config.get('common info', 'facebook_link')

    @staticmethod
    def getproduct_category_link():
        return config.get('common info', 'product_category_url')

    @staticmethod
    def get_men_product_link():
        return config.get('common info', 'men_product_link')

    @staticmethod
    def get_product_quantity():
        return config.get('common info', 'product_quantity')

    @staticmethod
    def getproduct_category2_link():
        return config.get('common info', 'product_category2_url')

    @staticmethod
    def get_outofstock_product_link():
        return config.get('common info', 'out_of_stock_product_link')

    @staticmethod
    def get_valid_keyword():
        return config.get('common info', 'valid_keyword')

    @staticmethod
    def get_invalid_keyword():
        return config.get('common info', 'invalid_keyword')

    @staticmethod
    def get_partial_keyword():
        return config.get('common info', 'partial_keyword')

    @staticmethod
    def get_filter_keyword():
        return config.get('common info', 'filter_keyword')

    @staticmethod
    def get_search_button():
        return config.get('common info', 'search_button')

    @staticmethod
    def get_category_link():
        return config.get('common info', 'category_link')

    @staticmethod
    def get_sub_category_link():
        return config.get('common info', 'sub_category_link')

    @staticmethod
    def get_women_product_link():
        return config.get('common info', 'women_product_link')

    @staticmethod
    def get_addtocart_button():
        return config.get('common info', 'addtocart_button')

    @staticmethod
    def get_updated_product_qty():
        return config.get('common info', 'product_qty')

    @staticmethod
    def get_cart_link():
        return config.get('common info', 'cart_link')

    @staticmethod
    def get_delete_btn():
        return config.get('common info', 'delete_btn')

    @staticmethod
    def get_coupon_code():
        return config.get('common info', 'coupon_code')

    @staticmethod
    def get_apply_btn():
        return config.get('common info', 'apply_btn_id')

    @staticmethod
    def get_invalid_coupon_code():
        return config.get('common info', 'invalid_coupon_code')

    @staticmethod
    def getShippingFirstName():
        return config.get('SHIPPING_INFO', 'first_name')

    @staticmethod
    def getShippingLastName():
        return config.get('SHIPPING_INFO', 'last_name')

    @staticmethod
    def getShippingAddress1():
        return config.get('SHIPPING_INFO', 'address_line')

    @staticmethod
    def getShippingCity():
        return config.get('SHIPPING_INFO', 'city')

    @staticmethod
    def getShippingCountry():
        return config.get('SHIPPING_INFO', 'country')

    @staticmethod
    def getShippingState():
        return config.get('SHIPPING_INFO', 'state')

    @staticmethod
    def getShippingZipcode():
        return config.get('SHIPPING_INFO', 'zipcode')

    @staticmethod
    def get_continue_button():
        return config.get('common info', 'continue_btn')

    @staticmethod
    def getCheckoutLink():
        return config.get('common info', 'checkout_link')

    @staticmethod
    def get_edit_button():
        return config.get('common info', 'edit_btn')

    @staticmethod
    def get_change_address_button():
        return config.get('common info', 'change_btn')

    @staticmethod
    def get_checkout_button():
        return config.get('common info', 'checkout_btn')

    @staticmethod
    def get_confirm_button():
        return config.get('common info', 'confirm_btn')

    @staticmethod
    def get_payment_button():
        return config.get('common info', 'edit_payment_btn')

    @staticmethod
    def get_checkbox_button():
        return config.get('common info', 'checkbox_btn')

    @staticmethod
    def get_order_continue_button():
        return config.get('common info', 'order_continue_btn')

    @staticmethod
    def get_my_account_link():
        return config.get('common info', 'my_account')

    @staticmethod
    def get_order_history_link():
        return config.get('common info', 'order_history')
















