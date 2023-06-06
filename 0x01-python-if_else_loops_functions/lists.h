#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Singly linked list
 * @n: Integer value stored in the node
 * @next: Pointer to the next node
 * Description: Node structure for a singly linked list
 * used in ALX project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
}
listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
