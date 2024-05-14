# import streamlit as st
# from streamlit_option_menu import option_menu
# import easyocr
# from PIL import Image
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import re
# import io
# import psycopg2

# def img_to_text(path):
#     image = []
#     input_IMG1 = Image.open(path)
#     input_IMG1_Array = np.array(input_IMG1)

#     language = easyocr.Reader(['en'])
#     text = language.readtext(input_IMG1_Array)

#     plt.imshow(input_IMG1_Array)
#     plt.axis('off')
#     plt.show()

#     for result in text:
#         image.append(result[1])        

#     return image, input_IMG1


# def extracting_data1(text):
#     dict1 = {"Name": [],
#              "Designation": [],
#              "Address": [],
#              "Telephone": [],
#              "Email ID": [],
#              "Website": [],
#              "Business Card": []
#              }
    
#     dict1['Name'].append(text[0])
#     dict1['Designation'].append(text[1])
#     # dict1['Address'].append(text[2])
#     # dict1['Pincode'].append(text[3])
#     # dict1['Telephone'].append(text[4])
#     # dict1['Email ID'].append(text[5])
#     # business_name = text[6] + ' ' + text[8]
#     # dict1['Business Name'].append(business_name)
#     # dict1['Design'].append(text[7])
# #my part
#     # for i in range(len(text)):
#     #     if text[i].startswith("+") or (text[i].replace("-", "").isdigit() and '-' in text[i]):
#     #         dict1["Telephone"].append(text[i])

#     #     elif "@" in text[i] and ".com" in text[i]:
#     #         dict1["Email ID"].append(text[i])

#     #     elif "WWW" in text[i] or "www" in text[i] or "Www" in text[i] or "wwW" in text[i] or "wWw" in text[i] or ".com" in text[i]:
#     #         normal = text[i].lower()
#     #         dict1["Website"].append(normal)

#     #     elif "Tamil Nadu" in text[i] or "TamilNadu" in text[i] or text[i].isdigit():
#     #         dict1["Address"].append(text[i])

#     #     elif re.match(r'^[A-Za-z]', text[i]):
#     #         dict1["Business Card"].append(text[i])

#     # return dict1

# #chatgpt
#     for i in range(len(text)):
#         if text[i].startswith("+") or (text[i].replace("-", "").isdigit() and '-' in text[i]):
#             dict1["Telephone"] = text[i]

#         elif "@" in text[i] and ".com" in text[i]:
#             dict1["Email ID"] = text[i]
#         elif "WWW" in text[i] or "www" in text[i] or "Www" in text[i] or "wwW" in text[i] or "wWw" in text[i] or ".com" in text[i]:
#             normal = text[i].lower()
#             dict1["Website"] = normal
#         elif "Tamil Nadu" in text[i] or "TamilNadu" in text[i] or text[i].isdigit():
#             dict1["Address"] = text[i]
#         elif re.match(r'^[A-Za-z]', text[i]):
#             dict1["Business Card"] = text[i]

#     for key, value in dict1.items():
#         if len(value)>0:
#             concad = " ".join(value)
#             dict1[key] = [concad]

#         else:
#             value = "N/A"
#             dict1[key] = [value]    


#     return dict1       


# #Streamlit Part
# st.title("BizCardX: Extracting Business Card Data with OCR")

# tabs = st.sidebar.selectbox(
#     "Navigation",
#     ["Home", "Extracting", "Modify"]
# )

# if tabs == "Home":
#     pass

# elif tabs == "Extracting":
#     insert = st.file_uploader("Upload the Image to Extract The Details", type=["png","jpg","jpeg"])
#     if insert:
#         image_text, input_image = img_to_text(insert)
#         pddf = extracting_data1(image_text)
#         df1= pd.DataFrame(pddf)
#         df1

#         st.image(input_image, caption='Uploaded Image.', use_column_width=True)
#         st.write("Extracted Text:")
#         st.write(image_text)
#         extracted_data = extracting_data1(image_text)
#         st.write("Extracted Data:")
#         st.write(extracted_data)
#         st.write("DataFrame".upper())
        
#         Img_Byte = io.BytesIO()
#         input_image.save(Img_Byte, format="PNG")
#         Img_data = Img_Byte.getvalue()
#         dict_data = {"Image Byte": [Img_data]}
#         df2 = pd.DataFrame(dict_data)

#         concatanation = pd.concat([df1,df2], axis= 1)
#         st.dataframe(concatanation)

#         st.button("Save")
#         connection = psycopg2.connect(
#         database="BizCard",
#         user="postgres",
#         password="kk07ch30",
#         host="localhost",
#         port="5432"
#     )

#     Mycursor = connection.cursor()

#     query = '''create table if not exists bizcard(
#     name varchar(300),
#     designation varchar(300),
#     address text,
#     telephone varchar(50),
#     email_id varchar(300),
#     website text,
#     business_card varchar(300),
#     Image_Byte BYTEA
#     )'''


#     Mycursor.execute(query)
#     connection.commit()

#     insert = '''insert into bizcard(
#     name,
#     designation,
#     address,
#     telephone,
#     email_id,
#     website,
#     business_card,
#     Image_Byte
#     )
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''


#     data = concatanation.values.tolist()

#     for row in data:
#         Mycursor.execute(insert, row)

#     connection.commit()

# elif tabs == "Modify":
#     pass





#Chatgpt
import streamlit as st
from streamlit_option_menu import option_menu
import easyocr
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import io
import psycopg2


def img_to_text(path):
    image = []
    input_IMG1 = Image.open(path)
    input_IMG1_Array = np.array(input_IMG1)

    language = easyocr.Reader(['en'])
    text = language.readtext(input_IMG1_Array)

    plt.imshow(input_IMG1_Array)
    plt.axis('off')
    plt.show()

    for result in text:
        image.append(result[1])        

    return image, input_IMG1

def extracting_data1(text):
    dict1 = {"Name": [],
             "Designation": [],
             "Address": [],
             "Telephone": [],
             "Email_ID": [],
             "Website": [],
             "Business_Card": []
             }
    
    dict1['Name'].append(text[0])
    dict1['Designation'].append(text[1])
    # dict1['Address'].append(text[2])
    # dict1['Pincode'].append(text[3])
    # dict1['Telephone'].append(text[4])
    # dict1['Email ID'].append(text[5])
    # business_name = text[6] + ' ' + text[8]
    # dict1['Business Name'].append(business_name)
    # dict1['Design'].append(text[7])

    for i in range(len(text)):
        if text[i].startswith("+") or (text[i].replace("-", "").isdigit() and '-' in text[i]):
            dict1["Telephone"].append(text[i])

        elif "@" in text[i] and ".com" in text[i]:
            dict1["Email_ID"].append(text[i])

        elif "WWW" in text[i] or "www" in text[i] or "Www" in text[i] or "wwW" in text[i] or "wWw" in text[i] or ".com" in text[i]:
            normal = text[i].lower()
            dict1["Website"].append(normal)

        elif "Tamil Nadu" in text[i] or "TamilNadu" in text[i] or text[i].isdigit():
            dict1["Address"].append(text[i])

        elif re.match(r'^[A-Za-z]', text[i]):
            dict1["Business_Card"].append(text[i])

        else:
            remove_colon = re.sub(r'[,;]','',text[i])
            dict1["Address"].append(remove_colon)

    for key, value in dict1.items():
        if len(value)>0:
            concad = " ".join(value)
            dict1[key] = [concad]

        else:
            value = "N/A"
            dict1[key] = [value]    
       


    return dict1

# Streamlit Part
st.title("BizCardX: Extracting Business Card Data with OCR")

tabs = st.sidebar.selectbox(
    "Navigation",
    ["Title", "EXTRACTING AND TRANSFERING", "MODIFYING & INSERTING"]
)

if tabs == "Title":
    pass

elif tabs == "EXTRACTING AND TRANSFERING":
    insert = st.file_uploader("Upload the Image to Extract The Details", type=["png", "jpg", "jpeg"])
    if insert:
        image_text, input_image = img_to_text(insert)
        pddf = extracting_data1(image_text)
        df1 = pd.DataFrame(pddf)

        st.image(input_image, caption='Uploaded Image.', use_column_width=True)
        st.write("Extracted Text:")
        st.write(image_text)
        st.write("Extracted Data:")
        st.write(pddf)
        st.write("DataFrame".upper())

        # Convert the image to bytes
        Img_Byte = io.BytesIO()
        input_image.save(Img_Byte, format="PNG")
        Img_data = Img_Byte.getvalue()

        # Add the image byte data to the DataFrame
        df1["Image_Byte"] = [Img_data]

        # Display the DataFrame
        st.dataframe(df1)

        if st.button("Transfer To SQL"):
            connection = psycopg2.connect(
                database="BizCard",
                user="postgres",
                password="kk07ch30",
                host="localhost",
                port="5432"
            )
            try:
                Mycursor = connection.cursor()

                query = '''create table if not exists bizcard(
                name varchar(300),
                designation varchar(300),
                address text,
                telephone varchar(50),
                email_id varchar(300),
                website text,
                business_card varchar(300),
                Image_Byte BYTEA
                )'''

                Mycursor.execute(query)
                connection.commit()

                insert = '''insert into bizcard(
                name,
                designation,
                address,
                telephone,
                email_id,
                website,
                business_card,
                Image_Byte
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

                data = df1.values.tolist()

                for row in data:
                    Mycursor.execute(insert, row)

                connection.commit()
                Mycursor.close()
                connection.close()

                st.success("Data saved successfully!")

            except Exception as e:
                st.error(f"An error occurred: {e}")
               

elif tabs == "MODIFYING & INSERTING":
    connection = psycopg2.connect(
        database="BizCard",
        user="postgres",
        password="kk07ch30",
        host="localhost",
        port="5432"
    )

    Mycursor = connection.cursor()

    select_query = "select * from bizcard"
    Mycursor.execute(select_query)
    table = Mycursor.fetchall()
    connection.commit()

    table_df = pd.DataFrame(table, columns=("name", "designation", "address", "telephone", "email_id",
                                            "website", "business_card", "Image_Byte"))

    selected_name = st.selectbox("Select The Name to Modify Its DataBase", table_df["name"])
    org_df = table_df[table_df["name"] == selected_name]
    st.write("ORIGINAL DATABASE")
    st.dataframe(org_df)
    modified_DF = org_df.copy()
    # st.write("MODIFIED DATA BASE")
    # st.dataframe(modified_DF)

    M_name = st.text_input("NAME", org_df["name"].unique()[0])
    M_desig = st.text_input("DESIGNATION", org_df["designation"].unique()[0])
    M_add = st.text_input("ADDRESS", org_df["address"].unique()[0])    
    M_tel = st.text_input("TELEPHONE", org_df["telephone"].unique()[0])    
    M_email = st.text_input("EMAIL ID", org_df["email_id"].unique()[0])    
    M_webs = st.text_input("WEBSITE", org_df["website"].unique()[0])    
    M_bz = st.text_input("BUSINESS CARD", org_df["business_card"].unique()[0])   
    M_ib = st.text_input("Image Byte", org_df["Image_Byte"].unique()[0])
    

    modified_DF["name "]= M_name
    modified_DF["designation "]= M_desig
    modified_DF["address "]= M_add
    modified_DF["telephone "]= M_tel
    modified_DF["email_id "]= M_name
    modified_DF["website "]= M_webs
    modified_DF["business_card "]= M_bz
    modified_DF["Image_Byte "]= M_ib

    st.write("MODIFIED DATA BASE")
    st.dataframe(modified_DF)

    if st.button("UPDATE", use_container_width=True):
        connection = psycopg2.connect(
        database="BizCard",
        user="postgres",
        password="kk07ch30",
        host="localhost",
        port="5432"
        )

        Mycursor = connection.cursor()
        Mycursor.execute(f"delete from bizcard where name = '{selected_name}'")
        connection.commit()
        
        inserting = '''insert into bizcard(
            name,
            designation,
            address,
            telephone,
            email_id,
            website,
            business_card,
            Image_Byte
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

        datas = modified_DF.values.tolist()[0]
        Mycursor.execute(inserting,datas)
        connection.commit()

        # st.write("MODIFIED DATA BASE")
        # st.dataframe(modified_DF)
        st.success("Modified Data saved successfully!")

    # Close the connection
    # Mycursor.close()
    # connection.close()









    
    
    
    
    
    
    





