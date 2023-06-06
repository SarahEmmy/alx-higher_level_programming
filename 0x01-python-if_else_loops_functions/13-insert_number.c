#include "lists.h"

/**
 * insert_node - inserts node a num into a sorted singly linked list.
 * @head: list head
 * @num: num to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *runner;
	listint_t *new;

	runner = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = num;

	if (*head == NULL || (*head)->n > num)
	{
		new->next = *head;
		*head = new;
		return(new);
	}

	while(runner->next != NULL)
	{
		if ((runner->next)->n >= num)
		{
			new->next = runner->next;
			runner->next = new;
			return(new);
		}
		runner = runner->next;
	}

	new->next = NULL;
	runner->next = new;
	return(new);
}
