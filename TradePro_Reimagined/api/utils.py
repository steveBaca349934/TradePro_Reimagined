from django.shortcuts import render

# def setup_user_injection(request:dict, html_name:str)->render:
#     """
#     Make every view have to implement the logic
#     of welcoming the user

#     Returns render
#     """
#     if request.session.get('logged_in') == True:

#         return render(request, f"home/{html_name}.html",{
#             "logged_in": True,
#             "user":request.session.get("user")

#         })

#     else:

#         return render(request, f"home/{html_name}.html",{
#             "logged_in": False

#         })
