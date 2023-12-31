import logging
import os
from flask import Flask
from flask_cors import CORS

from API.UserRoutes.CreateUserBlueprint import create_user_route
from API.UserRoutes.GetUserBlueprint import get_user_route
from API.UserRoutes.LoginBlueprint import login_route
from API.UserRoutes.LogoutBlueprint import logout_route
from API.UserRoutes.ChangeEmailBlueprint import change_email_route
from API.UserRoutes.ChangePasswordBlueprint import change_password_route
from API.UserRoutes.DeleteUserBlueprint import delete_user_route

from API.CategoryRoutes.CreateCategoryBlueprint import create_category_route
from API.CategoryRoutes.GetAllCategoriesBlueprint import get_all_categories_route
from API.CategoryRoutes.UpdateCategoryBlueprint import update_category_route
from API.CategoryRoutes.DeleteCategoryBlueprint import delete_category_route

from API.DepositRoutes.CreateDepositBlueprint import create_deposit_route
from API.DepositRoutes.GetAllDepositsBlueprint import get_all_deposits_route
from API.DepositRoutes.GetDepositsByCategoryBlueprint import get_deposits_by_category_route
from API.DepositRoutes.GetDepositsByDateBlueprint import get_deposits_by_date_route
from API.DepositRoutes.UpdateDepositBlueprint import update_deposit_route
from API.DepositRoutes.DeleteDepositBlueprint import delete_deposit_route

from API.ExpenseRoutes.CreateExpenseBlueprint import create_expense_route
from API.ExpenseRoutes.GetAllExpensesBlueprint import get_all_expenses_route
from API.ExpenseRoutes.GetExpensesByCategoryBlueprint import get_expenses_by_category_route
from API.ExpenseRoutes.GetExpensesByDateBlueprint import get_expenses_by_date_route
from API.ExpenseRoutes.UpdateExpenseBlueprint import update_expense_route
from API.ExpenseRoutes.DeleteExpenseBlueprint import delete_expense_route


def create_back_end_api(config):
    app: Flask = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    log_level = logging.DEBUG
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
    log_directory = os.path.join("Logs")
    os.makedirs(log_directory, exist_ok=True)
    log_file = os.path.join(log_directory, 'FinancialTrackingLogs.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    app.register_blueprint(create_user_route)
    app.register_blueprint(login_route)
    app.register_blueprint(logout_route)
    app.register_blueprint(get_user_route)
    app.register_blueprint(change_password_route)
    app.register_blueprint(change_email_route)
    app.register_blueprint(delete_user_route)

    app.register_blueprint(create_category_route)
    app.register_blueprint(get_all_categories_route)
    app.register_blueprint(update_category_route)
    app.register_blueprint(delete_category_route)

    app.register_blueprint(create_deposit_route)
    app.register_blueprint(get_all_deposits_route)
    app.register_blueprint(get_deposits_by_category_route)
    app.register_blueprint(get_deposits_by_date_route)
    app.register_blueprint(update_deposit_route)
    app.register_blueprint(delete_deposit_route)

    app.register_blueprint(create_expense_route)
    app.register_blueprint(get_all_expenses_route)
    app.register_blueprint(get_expenses_by_category_route)
    app.register_blueprint(get_expenses_by_date_route)
    app.register_blueprint(update_expense_route)
    app.register_blueprint(delete_expense_route)

    return app
