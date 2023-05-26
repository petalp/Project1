from docxtpl import DocxTemplate

doc = DocxTemplate("project3/invoice_gen.docx")

invoice_list = [[2, "pen", 0.5, 1],
                [1, "paper pack", 5, 5],
                [2, "notebook", 2, 4]]

doc.render({"name":"Peter", 
            "phone":"079567857", 
            "invoice_list":invoice_list,
            "subtotal":10,
            "salestax":"10%",
            "total":9})

doc.save("project3/new_invoice.docx")