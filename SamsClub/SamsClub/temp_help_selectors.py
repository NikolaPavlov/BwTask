product_title = product.css('div.sc-product-card-title span::text').get()
product_price = product.css('span.Price-group::attr(title)').get()
# TODO: need to pull multiple images
product_image = product.css('img.sc-product-card-image::attr(src)').get()
