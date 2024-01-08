#include "lists.h"


/**
 * is_palindrome - wach mandam ola la
 * @head: ras lkaaima dyalo
 * Return: walo ola wahad
 */


int is_palindrome(listint_t **head)

{

	if (head == NULL || *head == NULL)
	return (1);
	return (aux_palind(head, *head));

}


/**
 * aux_palind - dala dyal hadak
 * @head: rasse dyalo
 * @end: salat
 * Return: ya walo ya wahad
 */


int aux_palind(listint_t **head, listint_t *end)

{

	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{

		*head = (*head)->next;
		return (1);

	}
	return (0);

}
