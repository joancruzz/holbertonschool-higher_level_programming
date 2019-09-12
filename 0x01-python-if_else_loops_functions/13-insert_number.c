#include "lists.h"
/**
 * insert_mode - function that inserts number into a sorted singly linked list
 * @head: pointer to pointer of list
 * @number: value of node
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t  *prev, *node, *next = *head;
	node = malloc(sizeof(listint_t));
	if (node)
	{
		node->n = number;
		node->next = *head;
		if (!*head || number <= (*head)->n)
		{
			*head = node;
			return (node);
		}
		while (next && next->n < node->n)
		{
			prev = next;
			next = prev->next;
		}

		prev->next = node;
		node->next = next;
	}
	return (node);
}
