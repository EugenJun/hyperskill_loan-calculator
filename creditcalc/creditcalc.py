import math
import argparse


def start_loan_calculator():
    parser = argparse.ArgumentParser()

    parser.add_argument("--type", help="You should enter the type of payment", )
    parser.add_argument("--principal", type=int)
    parser.add_argument("--payment", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--periods", type=int)

    args = parser.parse_args()

    if args.type == 'annuity':
        if args.interest is None:
            print("Incorrect parameters.")
        elif args.principal is not None and args.payment is not None:
            i = (args.interest / 100) / (12 * 1)
            num_of_months = math.ceil(math.log(args.payment /
                                               (args.payment - i * args.principal), 1 + i))
            if num_of_months == 12:
                print("It will take 1 year to repay this loan!")
                print(f"Overpayment = "
                      f"{(num_of_months * args.payment) - args.principal}")
            elif num_of_months < 12:
                print(f"It will take {num_of_months} months to repay this loan!")
                print(f"Overpayment = "
                      f"{(num_of_months * args.payment) - args.principal}")
            elif num_of_months == 1:
                print("It will take 1 month to repay this loan!")
                print(f"Overpayment = "
                      f"{(num_of_months * args.payment) - args.principal}")
            elif num_of_months % 12 == 0:
                print(f"It will take {int(num_of_months / 12)} years to repay this loan!")
                print(f"Overpayment = "
                      f"{(num_of_months * args.payment) - args.principal}")
            else:
                print(f"It will take {int(num_of_months / 12)} years"
                      f" and {math.ceil(num_of_months % 12)} months to repay this loan!")
                print(f"Overpayment = "
                      f"{(num_of_months * args.payment) - args.principal}")
        elif args.principal is not None and args.periods is not None:
            i = (args.interest / 100) / (12 * 1)
            annuity_payment = \
                args.principal * (i * math.pow(1 + i, args.periods)) /\
                (math.pow(1 + i, args.periods) - 1)
            print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
            print(f"Overpayment = "
                  f"{(math.ceil(annuity_payment) * args.periods) - args.principal}")
        elif args.periods is not None and args.payment is not None:
            i = (args.interest / 100) / (12 * 1)
            loan_principal = args.payment / ((i * math.pow(1 + i, args.periods)) /
                                             (math.pow(1 + i, args.periods) - 1))
            print(f"Your loan principal = {math.floor(loan_principal)}!")
            print(f"Overpayment = "
                  f"{(args.payment * args.periods) - math.floor(loan_principal)}")
        else:
            pass

    elif args.type == 'diff':
        if args.principal is None or args.periods is None \
                or args.interest is None or args.payment is not None:
            print("Incorrect parameters.")
        else:
            i = (args.interest / 100) / (12 * 1)
            final_sum = 0
            for m in range(1, args.periods + 1):
                diff = (args.principal / args.periods) + i \
                       * (args.principal - (args.principal * (m - 1)) / args.periods)
                final_sum += math.ceil(diff)
                print(f"Month {m}: payment is {math.ceil(diff)}")

            print(f"\nOverpayment = {final_sum - args.principal}")

    else:
        print("Incorrect parameters.")


start_loan_calculator()
