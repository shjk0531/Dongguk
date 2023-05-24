using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Forever_ShowHeart : MonoBehaviour
{
    private void Update()
    {
        GetComponent<Text>().text = GameCounter.heart.ToString();
    }
}
