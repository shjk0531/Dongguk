using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SocialPlatforms.Impl;
using UnityEngine.UI;

public class Forever_ShowCount : MonoBehaviour
{
    private void Update()
    {
        this.gameObject.GetComponent<Text>().text = GameCounter.count.ToString();
    }
}
