# fail: #f1967f, success: #60c0bb
def help():
    help_message = f'''\
<html>

    <body style="font-family: monospace;">
    <table width="100%" border="0" cellspacing="20" cellpadding="10" bgcolor="#022130"; style="font-size: 20px; border-radius: 22px; color: #60c0bb">
        <tr>
            <td>
            <h1 style="text-align: center; font-size: 28px">AVAILABLE COMMANDS</h1>
            <h1 style="text-align: center; font-size: 20px;">-------------</h1>
            <table border = "1" style="margin: 0 auto; font-size: 16px;color: #60c0bb">
                <tr>
                    <th style="padding: 5px;">Command</th>
                    <th style="padding: 5px;">Description</th>
                </tr>
                <tr>
                    <td style="padding: 5px;">help</td>
                    <td style="padding: 5px;">Display help message</td>
                </tr>
                <tr>
                    <td style="padding: 5px;">shutdown</td>
                    <td style="padding: 5px;">Shutdown the computer</td>
                </tr>
                <tr>
                    <td style="padding: 5px;">screenshot</td>
                    <td style="padding: 5px;">Take a screenshot</td>
                </tr>
                <tr>
                    <td style="padding: 5px;">webcam</td>
                    <td style="padding: 5px;">Take a photo from webcam</td>
                </tr>
                <tr>
                    <td style="padding: 5px;">list_apps</td>
                    <td style="padding: 5px;">See running apps</td>
                </tr>
                <tr>
                    <td style="padding: 5px;">list_processes</td>
                    <td style="padding: 5px;">List all running processes</td>
                </tr>
                <tr>
                    <td style="padding: 5px;">kill_process &lt;pid&gt;</td>
                    <td style="padding: 5px;">Kill process with given pid</td>
                </tr>
                <tr>
                    <td style="padding: 5px;">keylog &lt;duration&gt; </td>
                    <td style="padding: 5px;">Start keylog</td>
                </tr>
            </table>
            </td>
        </tr>
    </table>
    </body>
</html>'''
    return help_message

def success_message(command):
    print(f'\nCommand executed successfully: {command}')
    img_tag = ''
    cmd_lst = ['screenshot', 'webcam']
    for cmd in cmd_lst:
        if command.startswith(cmd):
            img_tag ="""<img style="display: block; margin: 0 auto; border-radius: 22px" src="cid:image1" alt="image1">"""
            break
    message = f"""\
        <html>
    <body style="font-family: monospace;">
    <table width="100%" border="0" cellspacing="20" cellpadding="20" bgcolor="#022130" style="border-radius: 22px; color: #60c0bb">
        <tr>
            <td>
            <h1 style="text-align: center;">COMMAND SUCCESSFULLY EXECUTED</h1>
            <h1 style="text-align: center;">{command}</h1>
            {img_tag}
            </td>
        </tr>
    </table>
    </body>
</html>"""
    return message

def failure_message(command):
    message = f"""\
<html>

    <body style="font-family: monospace;">
    <table width="100%" border="0" cellspacing="20" cellpadding="20" bgcolor="#022130" style="border-radius: 22px; color: #f1967f">
        <tr>
            <td>
            <h1 style="text-align: center;">COMMAND FAILED TO EXECUTE</h1>
            <h1 style="text-align: center;">{command}</h1>
            <p style="text-align: center; font-size: 20px">Here's a croc instead</p>
            <img style="display: block; margin: 0 auto; border-radius: 22px;" src="cid:image1" alt="croc">

            </td>
        </tr>
    </table>
    </body>
</html>"""
    return message

def DataFormat(data, command):
    
    print(f'\nCommand executed successfully: {command}')
    data = data.strip().split('\n')
    header = data[0].split()
    processes = [line.split() for line in data[2:]]
    categories = {}
    for i in range(len(header)):
        categories[header[i]] = [process[i] for process in processes]
    del header
    del processes
    del data
    # format: {category: [list of values]}
    message = """\
<html> 
    <body style="font-family: monospace;">
    <table width="100%" border="0" cellspacing="20" cellpadding="10" bgcolor="#022130"; style="font-size: 20px; border-radius: 22px; color: #60c0bb">
        <tr>
            <td>
            <h1 style="text-align: center; font-size: 28px">RUNNING PROCESSES</h1>
            <h1 style="text-align: center; font-size: 20px;">-------------</h1>
            <table border = "1" style="margin: 0 auto; font-size: 16px;color: #60c0bb">
                <tr>
"""
    for key in categories.keys():
        message += f"<th style= \"padding: 5px\">{key}</th>\n"
    message += "</tr>\n"  # end of header row
    for key in categories.keys():
        tmp = key
        break
    for i in range(len(categories[tmp])):
        message += "<tr>\n"
        for key in categories.keys():
            message += f"<td style=\"padding: 5px;\">{categories[key][i]}</td>\n"
        message += "</tr>\n"
    # end of table
    message += f"""</table>
            </td>
        </tr>
            <td>
                <h1 style="text-align: center; font-size: 20px;">Total: {len(categories[tmp])}</h1>
            </td>
    </table>
    </body>
</html>
        """
    return message

def main():
    res = success_message('shutdown')
    res = success_message('kill_process')
    print(res)
    res = success_message('keylog')
    res = success_message('screenshot')
    
if __name__ == '__main__':
    main()