from app.usuario.controller import UserController
from app.movie.controller import MovieController
from app.lists.controller import ListController
from app.goal.controller import GoalController
from app.avaliacoes.controller import RatingController
from .view import MenuView


class ControlePrincipal:
    def __init__(self):
        self.user_controller = UserController()
        self.movie_controller = MovieController()
        self.menu_view = MenuView()
        self.list_controller = ListController()
        self.goal_controller = GoalController()
        self.avaliacoes_controller = RatingController()

    def inicializar(self):
        auth_user = self.user_controller.login()
        if not auth_user:
            return
        while True:
            self.goal_controller.check_goal(auth_user)
            self.user_controller.save_users()

            option = self.menu_view.menu_switch()
            if option == '0':
                change_account = self.user_controller.details(auth_user)
                if change_account:
                    auth_user = self.user_controller.login()
            elif option == '1':
                movie = self.movie_controller.search_movie()
                if movie:
                    add_to_list = self.movie_controller.movie_details(movie)
                    if add_to_list:
                        self.list_controller.add_item_to_list(movie, auth_user)
            elif option == '2':
                action = self.list_controller.menu(auth_user)
            elif option == '3':
                action = self.goal_controller.goal(auth_user)
            elif option == '4':
                action = self.avaliacoes_controller.add_rating(auth_user)
            else:
                return
        # while True:
        #     try:
        #         opcao = self.__tela_principal.menu_principal()

        #         if opcao != '0' and opcao != '1' and opcao != '2':
        #             exit()
        #         else:
        #             if opcao == '0':
        #                 reopcao = self.__tela_principal.menu_funcionario()

        #                 if reopcao == '0':
        #                     self.__controle_funcionario.adiciona_funcionario()
        #                 elif reopcao == '1':
        #                     self.__controle_funcionario.deleta_funcionario()
        #                 elif reopcao == '2':
        #                     self.__controle_funcionario.atualiza_funcionario()
        #                 elif reopcao == '3':
        #                     self.__controle_funcionario.funcionarios_cadastrados()
        #                 elif reopcao == '4':
        #                     self.__controle_funcionario.detalhes_do_funcionario()
        #                 elif reopcao == '5':
        #                     self.__controle_funcionario.adiciona_veiculo_funcionario()
        #                 elif reopcao == '6':
        #                     self.__controle_funcionario.deleta_veiculo_funcionario()

        #             elif opcao == '1':

        #                 reopcao = self.__tela_principal.menu_veiculo()

        #                 if reopcao == '0':
        #                     self.__controle_veiculo.lista_veiculos()
        #                 elif reopcao == '1':
        #                     self.__controle_veiculo.adiciona_veiculo()
        #                 elif reopcao == '2':
        #                     self.__controle_veiculo.detalhes_veiculo()
        #                 elif reopcao == '3':
        #                     self.__controle_veiculo.deleta_veiculo()
        #                 elif reopcao == '4':
        #                     self.__controle_veiculo.atualiza_veiculo()

        #             elif opcao == '2':

        #                 reopcao = self.__tela_principal.menu_movimentacao()

        #                 if reopcao == '0':
        #                     self.__controle_movimentacao.filtra_movimentacoes()
        #                 elif reopcao == '1':
        #                     self.__controle_movimentacao.acessos_por_tipo()
        #                 elif reopcao == '2':
        #                     self.__controle_movimentacao.retira_veiculo()
        #                 elif reopcao == '3':
        #                     self.__controle_movimentacao.devolve_veiculo()
        #     except Exception:
        #         pass
