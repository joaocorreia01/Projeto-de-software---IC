class Instructor:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise
        self.courses = []

    def create_course(self, title, description):
        new_course = Course(title, description, instructor=self)
        self.courses.append(new_course)
        return new_course

    def update_course(self, course, new_title=None, new_description=None):
        if course in self.courses:
            course.update(new_title, new_description)

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def manage_course(self, course):
        # falta implentar essa funcionalidade
        pass

class Course:
    def __init__(self, title, description, instructor):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.modules = []

    def update(self, new_title=None, new_description=None):
        if new_title:
            self.title = new_title
        if new_description:
            self.description = new_description

    def add_module(self, module):
        self.modules.append(module)

    def manage_enrollments(self):
        # Ainda falta sedenvolver essa funcionalidade de gerenciamento de inscrições
        pass

class Module:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

class Assignment:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.submissions = []

    def submit(self, student, submission_text):
        submission = Submission(student, submission_text)
        self.submissions.append(submission)

class Submission:
    def __init__(self, student, text):
        self.student = student
        self.text = text

class UserInterface:
    def __init__(self):
        self.instructor = None

    def start(self):
        print("Bem-vindo à Plataforma de Cursos!")

        instructor_name = input("Digite o nome do instrutor: ")
        instructor_expertise = input("Digite a especialidade do instrutor: ")
        self.instructor = Instructor(name=instructor_name, expertise=instructor_expertise)

        self.display_instructor_details()

        while True:

            print("\nOpções:")
            print("1. Criar Curso")
            print("2. Atualizar Informações do Curso")
            print("3. Atualizar Conteúdo do Módulo")
            print("4. Remover Conteúdo do Módulo")
            print("5. Adicionar Módulo")
            print("6. Remover Módulo")
            print("7. Mostrar Cursos e Módulos Criados")
            print("0. Sair")

            choice = input("Escolha uma opção (0-7): ")

            if choice == '1':
                self.create_course()
            elif choice == '2':
                self.update_course_information()
            elif choice == '3':
                self.update_module_content()
            elif choice == '4':
                self.remove_module_content()
            elif choice == '5':
                self.add_module()
            elif choice == '6':
                self.remove_module()
            elif choice == '7':
                self.display_created_courses_and_modules()
            elif choice == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def create_course(self):
 
        course_title = input("Digite o título do curso: ")
        course_description = input("Digite a descrição do curso: ")
        new_course = self.instructor.create_course(title=course_title, description=course_description)

        # Adição de módulos
        while True:
            module_title = input("Digite o título do módulo (ou pressione Enter para encerrar): ")
            if not module_title:
                break
            module_content = input("Digite o conteúdo do módulo: ")
            module = Module(title=module_title, content=module_content)
            new_course.add_module(module)

        self.display_course_details(new_course)

    def update_course_information(self):
        update_course_title = input("Digite o título do curso que deseja atualizar: ")

        # Verificando se o curso existe
        for course in self.instructor.courses:
            if update_course_title == course.title:

                new_course_title = input("Digite o novo título do curso (ou pressione Enter para manter o mesmo): ")

                new_course_description = input("Digite a nova descrição do curso (ou pressione Enter para manter a mesma): ")

                self.instructor.update_course(course, new_title=new_course_title, new_description=new_course_description)
                break
        else:
            print("Curso não encontrado. Não foi possível realizar a atualização.")

    def update_module_content(self):
        update_module_title = input("Digite o título do módulo que deseja atualizar: ")

        # Verificando se o módulo existe
        for course in self.instructor.courses:
            for module in course.modules:
                if update_module_title == module.title:
            
                    new_module_content = input("Digite o novo conteúdo do módulo (ou pressione Enter para manter o mesmo): ")

                    module.content = new_module_content
                    print(f"Conteúdo do módulo '{module.title}' atualizado com sucesso.")
                    break
            else:
                continue
            break
        else:
            print("Módulo não encontrado. Não foi possível realizar a atualização.")

    def remove_module_content(self):
        remove_module_title = input("Digite o título do módulo que deseja remover o conteúdo: ")

        # Verificando se o módulo existe
        for course in self.instructor.courses:
            for module in course.modules:
                if remove_module_title == module.title:
                    module.content = ""
                    print(f"Conteúdo do módulo '{module.title}' removido com sucesso.")
                    break
            else:
                continue
            break
        else:
            print("Módulo não encontrado. Não foi possível remover o conteúdo.")

    def add_module(self):
        
        if not self.instructor.courses:
            print("Não há cursos disponíveis para adicionar um módulo.")
            return

        print("Cursos disponíveis:")
        for i, course in enumerate(self.instructor.courses, 1):
            print(f"{i}. {course.title}")

        while True:
            try:
                course_index = int(input("Escolha o número do curso para adicionar o módulo: ")) - 1
                selected_course = self.instructor.courses[course_index]
                break
            except (ValueError, IndexError):
                print("Escolha inválida. Tente novamente.")

        module_title = input("Digite o título do novo módulo: ")
        module_content = input("Digite o conteúdo do novo módulo: ")
        new_module = Module(title=module_title, content=module_content)

        selected_course.add_module(new_module)
        print(f"Novo módulo '{new_module.title}' adicionado ao curso '{selected_course.title}' com sucesso.")

    def remove_module(self):

        if not self.instructor.courses:
            print("Não há cursos disponíveis para remover um módulo.")
            return

        print("Cursos disponíveis:")
        for i, course in enumerate(self.instructor.courses, 1):
            print(f"{i}. {course.title}")

        while True:
            try:
                course_index = int(input("Escolha o número do curso para remover o módulo: ")) - 1
                selected_course = self.instructor.courses[course_index]
                break
            except (ValueError, IndexError):
                print("Escolha inválida. Tente novamente.")


        print(f"Módulos disponíveis no curso '{selected_course.title}':")
        for i, module in enumerate(selected_course.modules, 1):
            print(f"{i}. {module.title}")


        while True:
            try:
                module_index = int(input("Escolha o número do módulo para remover: ")) - 1
                removed_module = selected_course.modules.pop(module_index)
                print(f"Módulo '{removed_module.title}' removido do curso '{selected_course.title}' com sucesso.")
                break
            except (ValueError, IndexError):
                print("Escolha inválida. Tente novamente.")

    def display_course_details(self, course):
        print("\nDetalhes do Curso:")
        print(f"Título: {course.title}")
        print(f"Descrição: {course.description}")
        print("Módulos:")
        for module in course.modules:
            print(f"  - {module.title}: {module.content}")

    def display_created_courses_and_modules(self):
        print("\nCursos e Módulos Criados:")
        for course in self.instructor.courses:
            self.display_course_details(course)

    def display_instructor_details(self):
        print("\nDetalhes do Instrutor:")
        print(f"Nome: {self.instructor.name}")
        print(f"Especialidade: {self.instructor.expertise}")
        print("Cursos:")
        for course in self.instructor.courses:
            print(f"  - {course.title}")


ui = UserInterface()


ui.start()
