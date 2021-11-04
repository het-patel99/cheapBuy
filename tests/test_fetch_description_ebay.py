from ..code.web.scraper.fetch_description.ebay import description_from_url_ebay


def test_fetch_description_ebay():
    link = "https://www.ebay.com/itm/224549626866?_trkparms=ispr%3D5&hash=item34483363f2:g:3S8AAOSww65hAZwc&amdata" \
           "=enc%3AAQAGAAACYPYe5NmHp" \
           "%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsSvtkx670Z0mbyfWqmxLFLYUM9eowcHtgHE5ytksUIxDId9cd7xuCMq0Az0iTNXVt6LJ" \
           "mzJkYBmleZIBrJyv04UL4loWvjv2ozK%252FZQe6SFdEgronR21fgQU2yklw8N3J%252FB8TUyT%252FGQS5t4Hr%252BHy%252BWn" \
           "bkUaoAvnAmilRVdpvnQzyyowIWSRfR6GqGBeD3UePbWGfqNgDWk9QwhFMSCha8HyCTzAPHu841OcS%252B1h6eUfwAnmYb4rHfd1bK" \
           "Y16mRHZaljkNsLclNfMQPRuee9UEASuShn6hym1vl0tGhcuSBRpyzNbkjwfj7WRabrByGNFcVhBUeDmDVuUMjbFk207cw5cNh7utXa" \
           "B7rrAgA7pzWwAFjorV%252F1b9%252Br6LhsJk6w8TpWWMEXhREAjE9bNWjJnDiqXixljRKMptHPUOy6irv8N5gbUodaTCqAK9VRPU" \
           "AkS2D%252FG2v%252FvMr%252FuwWosuQukHbBPoFYrVHWJfQFDB%252FATpMG%252Fw3fwd2BXetQ28ayrfsHZ3RUXyXWD7NtqN9n" \
           "nMC0XUeH24MC8VCTEd2AWgHkCpRv9HBP3KCLumycks%252BUVduwFDXE0SoxNObdemkgzwSyshqpcYQbfSHHxH0NmuBDZraU6GxI9D" \
           "mXbxKlY8QirR15LoqiZRcIcYkogfgFDMkCSdU11%252BnfGOor8iyKktHZ5uR%252BovgsSlE55taNpF9IAmLSArp5P1EKEm%252Bkh" \
           "EwcmwA%252BHsI7QySx8ri99Hxu6O62wOyP80ltapkPZkco8DWx95Ft1JXh%7Cclp%3A2334524%7Ctkp%3ABlBMUP7JxbydXw"
    description = description_from_url_ebay(link)
    assert (description.title == 'PS5 IN HAND - NEW Playstation 5 Digital Edition White Console System LATEST'
            and description.price == '899.00')
