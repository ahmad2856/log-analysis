# !/usr/bin/env python

import psycopg2


question_1 = "1. What are the most popular three articles of all time?"

query_1 = ("SELECT title, count(*) as views FROM articles \n"
           "  JOIN log\n"
           "    ON articles.slug = substring(log.path, 10)\n"
           "    GROUP BY title ORDER BY views DESC LIMIT 3;")

question_2 = "2. Who are the most popular article authors of all time?"

query_2 = ("SELECT authors.name, count(*) as views\n"
           "    FROM articles \n"
           "    JOIN authors\n"
           "      ON articles.author = authors.id \n"
           "      JOIN log \n"
           "      ON articles.slug = substring(log.path, 10)\n"
           "      WHERE log.status LIKE '200 OK'\n"
           "      GROUP BY authors.name ORDER BY views DESC;")

query3 = "select * from error_logs_view where \"Percent Error\" > 1"

result3 = dict()
result3['title'] = \
    """
3. On which days did more than 1% of requests lead to errors?
"""


# Connect to News_db
def get_results(sql_query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

result1 = get_results(query_1)
result2 = get_results(query_2)
result3['results'] = get_results(query3)


# print results of the query
def print_error_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' %')


def print_results(q_list):
    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")
    print("\n")

print(question_1)
print_results(result1)
print(question_2)
print_results(result2)
print_error_query_results(result3)
