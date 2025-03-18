
def format_number(num):
    if num > 1000000:
        if not num % 1000000:
            return f'{num // 1000000} M'
        return f'{round(num / 1000000, 1)} M'
    return f'{num // 1000} K'


def col_design(title, value) : 
    html = f"""
                <div style="border: 2px solid #2ECC71; padding: 10px; margin-bottom: 20px;">
                    <h3 style="font-size: 24px; text-align: center; color: #4CAF50;"> {title} </h3>
                    <p style="font-size: 18px; text-align: center;"> {value} </p>
                </div>
                """
    return html
