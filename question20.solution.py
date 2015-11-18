from argparse import ArgumentParser

def main():
    """Example function for parsing command line arguments"""
    parser = ArgumentParser(description="Solution to question 20 from the practice problems")
    parser.add_argument(
        '--required_num_arg', type=float, required=True,
        help='A numerical argument in floating point format') 
    parser.add_argument(
        '--optional_str_arg', type=str, required=False,
        default='this_is_the_default_value',
        help='A numerical argument in floating point format') 
    args = parser.parse_args()
    print('{} {}'.format(args.required_num_arg, args.optional_str_arg))

if __name__ == '__main__':
    main()
