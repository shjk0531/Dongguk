using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class DestroyObject : MonoBehaviour
{
    [SerializeField] private string thisType;

    public int score;
    public int atk;


    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.GetComponent<Player>())
        {
            if(thisType == "item")
            {
                GameCounter.count += score;
                this.gameObject.SetActive(false);
            }
            if (thisType == "enemy")
            {
                GameCounter.heart -= atk;
            }
        }

        if (collision.gameObject.GetComponent<Weapon>())
        {
            if (thisType == "item")
            {
                collision.gameObject.SetActive(false);
                this.gameObject.SetActive(false) ;
            }
            if (thisType == "enemy")
            {
                GameCounter.count += score;
                collision.gameObject.SetActive(false) ;
                this.gameObject.SetActive(false);
            }
        }
    }
}
